# PyQt5

Core Python concepts, exercises, and PyQt5 GUI practice, all in one folder. Each `.py` file is a standalone script covering a specific topic or mini-project.

This folder covers the general Python + PyQt5-GUI side of my practice within [`Py_learning`](../); for game-development practice, see the sibling [`pygame`](../pygame) folder instead.

## 📁 What's Inside

**Core language concepts**
- `for_loops.py`, `while_loops.py`, `nested_loops.py` — loop constructs
- `functions.py`, `decorators.py` — functions and decorators
- `lists.py`, `tuple.py`, `set.py`, `dictionary.py`, `collections_2dlists.py`, `my_collections.py` — built-in data structures
- `string_indexing.py`, `format_specifiers.py` — string handling and formatting
- `date_time.py`, `random_num.py` — standard library basics

**Object-oriented programming**
- `my_class.py`, `class_variables.py`, `class_methods.py`, `static_methods.py`
- `inheritance.py`, `multi_inheritance.py`, `super.py`, `polymorphism.py`
- `magic_methods.py`, `dukc_typing.py`, `property.py`
- `project_oriented_programming.py`, `exceptions.py`

**Concurrency & I/O**
- `multithreading.py`
- `file_work/` — subfolder covering reading/writing text, CSV, and JSON files (`read_files.py`, `writting_files.py`, `file_detection.py`, plus sample `test`, `test.csv`, `test.json` data files)

**GUI programming (PyQt5)**
- `GUI.py`, `GUI_buttons.py`, `GUI_checkboxes.py`, `GUI_images.py`, `GUI_labels.py`, `GUI_layot.py`, `GUI_line_edit.py`, `GUI_radiobuttons.py` — `GUI.py` and `GUI_images.py` load `21593.jpg` as a sample image
- `CSS_style.py` — styling PyQt widgets
- `digital_clock.py`, `alarm_clock.py`, `StopWhatch.py`, `countdown_timer_program.py`, `weather_app.py` — small GUI apps (`digital_clock.py` uses the `DS-DIGIT.TTF` font asset; `alarm_clock.py` plays `my_music.wav` as its alarm sound)

**Networking**
- `API_request.py` — making HTTP requests to an external API

**Practice programs / mini-games**
- `hangman_game.py` (uses `wordslist.py` for its word list)
- `number_guessing_game.py`, `quiz_game.py`, `rock_paper_scizors.py`, `slot_machine.py`
- `banking_program.py`, `shoping_cart_program.py`, `concession_stand_program.py`, `compound_interest_calculator.py`
- `encryption.py`, `test.py`

## ⚙️ Requirements

```bash
pip install PyQt5 requests
```

## 🚀 Running

```bash
python3 <filename>.py
```

Some scripts depend on a sibling file/asset in this same folder (e.g. `hangman_game.py` imports `wordslist.py`; `GUI.py` loads `21593.jpg`) — run them from within this folder so the relative paths resolve correctly.

<sub>Note: written while following Bro Code's Python tutorials on YouTube; original teaching content © Bro Code.</sub>
