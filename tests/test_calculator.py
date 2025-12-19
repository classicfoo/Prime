import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.calculator import Calculator, CalculatorError


def test_basic_percentage_conversion():
    calc = Calculator()
    assert calc.calculate("50%") == pytest.approx(0.5)
    assert calc.calculate("12.5%") == pytest.approx(0.125)


def test_percentage_in_expression():
    calc = Calculator()
    assert calc.calculate("200 * 10%") == pytest.approx(20)
    assert calc.calculate("100 + 5%") == pytest.approx(100.05)


def test_unary_operations_and_parentheses():
    calc = Calculator()
    assert calc.calculate("-(50%)") == pytest.approx(-0.5)
    assert calc.calculate("(25% + 25%) * 4") == pytest.approx(2)


def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(CalculatorError, match="Division by zero"):
        calc.calculate("5/0")


def test_invalid_expression():
    calc = Calculator()
    with pytest.raises(CalculatorError):
        calc.calculate("2 + foo")
