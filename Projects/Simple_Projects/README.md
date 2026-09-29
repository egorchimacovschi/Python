# Simple_Projects

Small standalone Python applications, each in its own file, built with the concepts practiced in [`Py_learning`](../../Py_learning). For a larger, multi-file project, see the sibling [`AI_FLAPPY_BIRDS`](../AI_FLAPPY_BIRDS) folder.

## 📁 What's Inside

| File | Description |
|---|---|
| `digital_clock.py` | A PyQt5 desktop app that displays a live digital clock, using a custom digital-style font (`DS-DIGIT.TTF`) |
| `weather_app.py` | A PyQt5 desktop app that takes a city name as input and displays the current weather (temperature, condition, emoji) by calling a weather API |
| `DS-DIGIT.TTF` | Custom font asset used by `digital_clock.py` for the digit display |

`__pycache__/` contains auto-generated Python bytecode cache files and can be safely ignored or deleted.

## ⚙️ Requirements

```bash
pip install PyQt5 requests
```

## 🚀 Running

```bash
python3 digital_clock.py
python3 weather_app.py
```

`weather_app.py` calls an external weather API, so an internet connection (and, depending on the provider, an API key configured in the script) is required.
