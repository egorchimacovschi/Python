# Projects

More complete, standalone applications built on top of what was learned in [`Py_learning`](../Py_learning) — each one is its own multi-file project rather than a single practice script.

## 📁 What's Inside

| Folder | Content |
|---|---|
| [`Simple_Projects`](./Simple_Projects) | Small single-file PyQt5 desktop apps: a digital clock and a weather app |
| [`AI_FLAPPY_BIRDS`](./AI_FLAPPY_BIRDS) | A Flappy-Bird clone built in pygame, structured into a `scripts/` package, with animated sprites, scrolling pipes, scoring, and a restart button |

Each subfolder has its own `README.md` with a full breakdown of what's inside and how to run it.

## ⚙️ Requirements

```bash
pip install PyQt5 requests pygame
```

## 🚀 Running

```bash
cd Simple_Projects
python3 digital_clock.py

cd ../AI_FLAPPY_BIRDS
python3 flappy_birds.py
```

Run each project from inside its own folder — they load their asset files (fonts, images) using paths relative to that folder.
