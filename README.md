# Prime

A Qt-inspired calculator implemented in Python. The calculator can evaluate
simple arithmetic expressions, supports percentage values, and now includes a Qt
GUI built with PyQt6.

## Usage (GUI)

### Library

```

Type expressions directly into the display (or use the on-screen buttons) and
press **Enter** or click **=** to evaluate.

Alternatively, you can launch the window with:

```
python -m src.gui
```

### Qt GUI

```
python -m src.gui
```

Ensure `PyQt6` is installed (use `pip install -r requirements.txt` if needed).

## Running tests

```
pip install -r requirements.txt  # if needed
pytest
```
