// Tiny API that stores "Sen Çiz" drawings in personal galleries (Cloudflare Worker + D1).
// Reads are public to anyone holding the unguessable gallery id; writes need the gallery secret.

const ALLOWED_ORIGINS = [
  "https://ardazeybek-dev.github.io",
  "http://localhost:8765",
  "http://127.0.0.1:8765",
];
const MAX_BODY = 1_500_000;
const MAX_DRAWINGS = 300;
const ID_CHARS = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789";

function newId(len) {
  const bytes = crypto.getRandomValues(new Uint8Array(len));
  return Array.from(bytes, (b) => ID_CHARS[b % ID_CHARS.length]).join("");
}

async function sha256(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return Array.from(new Uint8Array(buf), (b) => b.toString(16).padStart(2, "0")).join("");
}

function cors(origin) {
  const allow = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allow,
    "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Max-Age": "86400",
    Vary: "Origin",
  };
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", ...cors(origin) },
  });
}

async function readBody(request) {
  const text = await request.text();
  if (text.length > MAX_BODY) throw new HttpError(413, "Çizim çok büyük");
  try {
    return JSON.parse(text);
  } catch {
    throw new HttpError(400, "Geçersiz veri");
  }
}

class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

async function requireOwner(env, request, gid) {
  const auth = request.headers.get("Authorization") || "";
  const secret = auth.startsWith("Bearer ") ? auth.slice(7) : "";
  const row = await env.DB.prepare("SELECT secret_hash FROM galleries WHERE id = ?").bind(gid).first();
  if (!row) throw new HttpError(404, "Galeri bulunamadı");
  if (!secret || (await sha256(secret)) !== row.secret_hash) throw new HttpError(403, "Bu galeriye yazma iznin yok");
}

function cleanText(value, max) {
  return String(value ?? "").replace(/[\u0000-\u001f]/g, " ").trim().slice(0, max);
}

async function handle(request, env) {
  const url = new URL(request.url);
  const parts = url.pathname.split("/").filter(Boolean);
  const method = request.method;

  if (parts[0] !== "api") throw new HttpError(404, "Yok");

  // POST /api/galleries
  if (method === "POST" && parts.length === 2 && parts[1] === "galleries") {
    const body = await readBody(request);
    const id = newId(10);
    const secret = newId(32);
    await env.DB.prepare("INSERT INTO galleries (id, name, secret_hash, created) VALUES (?, ?, ?, ?)")
      .bind(id, cleanText(body.name, 40), await sha256(secret), Date.now())
      .run();
    return { status: 201, body: { id, secret } };
  }

  // GET /api/galleries/:gid
  if (method === "GET" && parts.length === 3 && parts[1] === "galleries") {
    const gallery = await env.DB.prepare("SELECT id, name, created FROM galleries WHERE id = ?").bind(parts[2]).first();
    if (!gallery) throw new HttpError(404, "Galeri bulunamadı");
    const { results } = await env.DB.prepare(
      "SELECT id, title, created FROM drawings WHERE gallery = ? ORDER BY created DESC"
    ).bind(parts[2]).all();
    return { status: 200, body: { ...gallery, drawings: results } };
  }

  // POST /api/galleries/:gid/drawings
  if (method === "POST" && parts.length === 4 && parts[1] === "galleries" && parts[3] === "drawings") {
    const gid = parts[2];
    await requireOwner(env, request, gid);
    const body = await readBody(request);
    if (!Array.isArray(body.strokes) || body.strokes.length === 0) throw new HttpError(400, "Boş çizim");
    const count = await env.DB.prepare("SELECT COUNT(*) AS n FROM drawings WHERE gallery = ?").bind(gid).first("n");
    if (count >= MAX_DRAWINGS) throw new HttpError(409, "Galeri dolu");
    const id = newId(10);
    await env.DB.prepare("INSERT INTO drawings (id, gallery, title, created, data) VALUES (?, ?, ?, ?, ?)")
      .bind(id, gid, cleanText(body.title, 60), Date.now(), JSON.stringify({ strokes: body.strokes }))
      .run();
    return { status: 201, body: { id } };
  }

  // GET /api/drawings/:id
  if (method === "GET" && parts.length === 3 && parts[1] === "drawings") {
    const row = await env.DB.prepare("SELECT id, gallery, title, created, data FROM drawings WHERE id = ?")
      .bind(parts[2]).first();
    if (!row) throw new HttpError(404, "Çizim bulunamadı");
    return { status: 200, body: { ...row, data: JSON.parse(row.data) } };
  }

  // DELETE /api/galleries/:gid/drawings/:id
  if (method === "DELETE" && parts.length === 5 && parts[1] === "galleries" && parts[3] === "drawings") {
    await requireOwner(env, request, parts[2]);
    await env.DB.prepare("DELETE FROM drawings WHERE id = ? AND gallery = ?").bind(parts[4], parts[2]).run();
    return { status: 200, body: { ok: true } };
  }

  throw new HttpError(404, "Yok");
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors(origin) });
    try {
      const { status, body } = await handle(request, env);
      return json(body, status, origin);
    } catch (err) {
      if (err instanceof HttpError) return json({ error: err.message }, err.status, origin);
      console.error(err);
      return json({ error: "Sunucu hatası" }, 500, origin);
    }
  },
};
