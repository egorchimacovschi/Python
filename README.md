# Python

My dedication to Python — a personal collection of exercises, mini-programs, and small GUI/data projects.

## 📁 Repository Structure

| Folder | Content |
|---|---|
| [`Py_learning`](./Py_learning) | Core Python concepts: loops, functions, OOP, collections, decorators, file I/O, GUI (PyQt), and small practice games/programs |
| [`Projects`](./Projects) | Slightly more complete standalone applications (digital clock, weather app) built on top of what was learned in `Py_learning` |

Each folder has its own `README.md` with more detail on what's inside.

## ⚙️ Requirements

- Python 3
- pip

Some scripts (GUI apps, weather app) require extra packages such as `PyQt5` and `requests`:

```bash
pip install PyQt5 requests
```

## 🚀 Running

Each file is a standalone script. Run any of them directly with:

```bash
python3 <folder>/<file>.py
```

## 📌 Notes

- This repository is a personal learning log and grows as new topics are covered.
- Files are individual exercises/labs; most don't depend on each other, aside from a few that import a shared helper module (e.g. `wordslist.py`, `my_class.py`) from within the same folder.

## ✍️ Author

Maintained by Egor as part of ongoing Python coursework.

<sub>Note: Some exercises here were written while following Bro Code's Python tutorials on YouTube; original teaching content © Bro Code.</sub>
