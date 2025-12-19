# Prime

A Qt-inspired calculator implemented in Python. The calculator can evaluate
simple arithmetic expressions, supports percentage values, and now includes a Qt
GUI built with PyQt6.

## Usage

### Library

```
python - <<'PY'
from src.calculator import Calculator

calc = Calculator()
print(calc.calculate("200 * 10%"))  # 20.0
print(calc.calculate("100 + 5%"))   # 100.05
PY
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
