# Py_learning

Core Python practice, split into two tracks: general-purpose language/GUI concepts (`PyQt5`) and game-development practice (`pygame`).

## 📁 What's Inside

| Folder | Content |
|---|---|
| [`PyQt5`](./PyQt5) | Core Python concepts (loops, OOP, collections, file I/O, decorators, multithreading), small practice games, and PyQt5 GUI programs |
| [`pygame`](./pygame) | Game-development practice with pygame: a tile-based platformer built by following a tutorial |

Each subfolder has its own `README.md` with a full breakdown of what's inside.

## ⚙️ Requirements

```bash
pip install PyQt5 requests pygame
```

Not every file needs every package — see each subfolder's README for specifics.

## 🚀 Running

```bash
python3 PyQt5/<file>.py
```

The pygame project loads its assets using paths relative to its own folder, so run it from inside `pygame/pygame_example_tutorial/` instead — see that folder's README for exact steps.
