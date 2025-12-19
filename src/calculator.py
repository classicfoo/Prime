"""Core calculator logic with percentage support."""
from __future__ import annotations

import ast
import operator
import re
from typing import Callable, Dict


_ALLOWED_BIN_OPS: Dict[type, Callable[[float, float], float]] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

_ALLOWED_UNARY_OPS: Dict[type, Callable[[float], float]] = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


class CalculatorError(ValueError):
    """Raised when an invalid expression is provided to the calculator."""


class Calculator:
    """Evaluate arithmetic expressions with percentage support.

    The calculator accepts the four basic operators (``+``, ``-``, ``*``, ``/``)
    and interprets the percentage symbol as dividing the preceding number by 100.
    For example, ``50%`` becomes ``0.5`` and ``200 * 10%`` becomes ``20``.
    """

    percent_pattern = re.compile(r"(\d+(?:\.\d+)?)%")

    def calculate(self, expression: str) -> float:
        """Evaluate the given arithmetic expression.

        Args:
            expression: The expression to evaluate.

        Returns:
            The numeric result of the expression.

        Raises:
            CalculatorError: If the expression contains unsupported syntax.
        """

        cleaned = expression.strip()
        cleaned = self._handle_percentage(cleaned)
        try:
            tree = ast.parse(cleaned, mode="eval")
        except SyntaxError as exc:  # pragma: no cover - converted to CalculatorError
            raise CalculatorError(str(exc)) from exc

        return self._eval_node(tree.body)

    def _handle_percentage(self, expression: str) -> str:
        """Replace percent expressions with their decimal equivalents."""

        def replacer(match: re.Match[str]) -> str:
            number = float(match.group(1))
            return str(number / 100)

        return self.percent_pattern.sub(replacer, expression)

    def _eval_node(self, node: ast.AST) -> float:
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BIN_OPS:
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            try:
                return _ALLOWED_BIN_OPS[type(node.op)](left, right)
            except ZeroDivisionError as exc:  # pragma: no cover - propagate as CalculatorError
                raise CalculatorError("Division by zero") from exc

        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARY_OPS:
            operand = self._eval_node(node.operand)
            return _ALLOWED_UNARY_OPS[type(node.op)](operand)

        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)

        raise CalculatorError(f"Unsupported expression component: {ast.dump(node)}")
