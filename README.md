# Prime

A Qt-inspired calculator core implemented in Python. The calculator can evaluate
simple arithmetic expressions and now supports percentage values.

## Usage

```
python - <<'PY'
from src.calculator import Calculator

calc = Calculator()
print(calc.calculate("200 * 10%"))  # 20.0
print(calc.calculate("100 + 5%"))   # 100.05
PY
```

## Running tests

```
pip install -r requirements.txt  # if needed
pytest
```
