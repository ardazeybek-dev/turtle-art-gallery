CREATE TABLE IF NOT EXISTS galleries (
  id TEXT PRIMARY KEY,
  name TEXT,
  secret_hash TEXT NOT NULL,
  created INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS drawings (
  id TEXT PRIMARY KEY,
  gallery TEXT NOT NULL REFERENCES galleries(id),
  title TEXT,
  created INTEGER NOT NULL,
  data TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_drawings_gallery ON drawings (gallery, created);
