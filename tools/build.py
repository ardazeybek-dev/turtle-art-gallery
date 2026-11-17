"""Runs every drawings/*.py against the recording turtle and writes docs/data/."""
import json
import pathlib
import random
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import fake_turtle  # noqa: E402

sys.modules["turtle"] = fake_turtle
time.sleep = lambda s: None

out = ROOT / "docs" / "data"
out.mkdir(parents=True, exist_ok=True)
manifest = []
failed = []

for i, path in enumerate(sorted((ROOT / "drawings").glob("*.py")), 1):
    code = path.read_text(encoding="utf-8")
    title = code.splitlines()[0].lstrip("# ").strip()
    fake_turtle.REC.reset()
    fake_turtle.Turtle._ids = 0
    random.seed(7)
    try:
        exec(compile(code, str(path), "exec"), {"__name__": "__main__"})
    except Exception as e:  # report every broken script, not just the first
        failed.append(f"{path.name}: {type(e).__name__}: {e}")
        continue
    rec = fake_turtle.REC
    if rec.segments == 0:
        failed.append(f"{path.name}: draws nothing")
        continue
    xs, ys = [], []
    for op in rec.ops:
        if op[0] == 0:
            xs += op[1::2]
            ys += op[2::2]
        elif op[0] == 4:
            xs += op[2][0::2]
            ys += op[2][1::2]
        elif op[0] in (3, 5):
            xs.append(op[1])
            ys.append(op[2])
    hw, hh = rec.size[0] / 2, rec.size[1] / 2
    bbox = (min(xs), max(xs), min(ys), max(ys))
    if bbox[0] < -hw or bbox[1] > hw or bbox[2] < -hh or bbox[3] > hh:
        print(f"   !! {path.name} leaves the screen: x {bbox[0]}..{bbox[1]} y {bbox[2]}..{bbox[3]}")
    name = f"{i:02d}.json"
    data = {"bg": rec.bg, "w": rec.size[0], "h": rec.size[1], "ops": rec.ops}
    (out / name).write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    manifest.append({"title": title, "file": name, "py": path.name, "steps": rec.segments,
                     "bg": rec.bg, "code": code})
    print(f"{i:02d} {rec.segments:6d} steps {(out / name).stat().st_size // 1024:5d} KB  {title}")

(out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False), encoding="utf-8")
total = sum(f.stat().st_size for f in out.glob("*.json"))
print(f"\n{len(manifest)} drawings, data total {total // 1024} KB")
if failed:
    print("\nFAILED:\n  " + "\n  ".join(failed))
    sys.exit(1)
