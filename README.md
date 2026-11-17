# Turtle Art Gallery 🐢

77 drawings made with Python's `turtle` module, replayed live in the browser next to the exact code that produced them. Browse with ← / →, or switch to **Sen Çiz** to draw with mirror symmetry (as lines or as ASCII characters) and get the Python turtle code for your own drawing.

**Live:** https://ardazeybek-dev.github.io/turtle-art-gallery/

## How it works

1. Every drawing is a plain Python script in `drawings/` that runs with real `turtle`.
2. `tools/build.py` runs each script against `tools/fake_turtle.py`, a strict stand-in that records every line, dot, fill and text instead of opening a window.
3. The recordings go to `docs/data/` (one JSON per drawing + `manifest.json` with titles and source code).
4. `docs/index.html` replays a recording on a canvas and shows the source beside it. "Video indir" renders the same replay frame by frame into a 1080×1920 MP4 in the browser (WebCodecs + mediabunny, loaded only when used).

The fake turtle raises on any call or color name real turtle would not accept the same way, so the code shown on the site always runs on a desktop.

## Run locally

```bash
python tools/build.py            # rebuild docs/data after changing a drawing
cd docs && python -m http.server 8765
# open http://localhost:8765
```

Run a single drawing in real turtle: `python drawings/02_kalp_isinlari.py`

No environment variables, no dependencies beyond Python 3.

## Adding a drawing

Create `drawings/NN_name.py`. The first line is the title (`# Title`). Use `s.setup(700, 700)`, then run `python tools/build.py`; it warns if anything leaves the 700×700 screen.

## Layout

```
drawings/        Python turtle scripts (source of truth)
tools/           fake_turtle.py recorder + build.py
docs/            GitHub Pages site (index.html + generated data/)
```

## Pitfalls

- Color looks different on the site than in Python → Tk and CSS disagree on `gray`, `green`, `maroon`, `purple` → use hex; the build rejects those names.
- Fill hides half of the outline → real turtle puts the fill polygon below the lines drawn after `begin_fill` → the recorder inserts the fill at `begin_fill` time, keep it that way.
- Random drawings differ from the site when run locally → the build seeds `random` with 7 → expected, every run is a new variant.
