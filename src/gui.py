"""Qt GUI calculator leveraging the calculator core."""
from __future__ import annotations

import sys
from typing import Iterable

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.calculator import Calculator, CalculatorError


class CalculatorWindow(QWidget):
    """A simple Qt calculator window."""

    button_order: Iterable[tuple[str, int, int]] = (
        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("/", 0, 3),
        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("*", 1, 3),
        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("-", 2, 3),
        ("0", 3, 0),
        (".", 3, 1),
        ("%", 3, 2),
        ("+", 3, 3),
        ("(", 4, 0),
        (")", 4, 1),
        ("⌫", 4, 2),
        ("C", 4, 3),
        ("=", 5, 0),
    )

    def __init__(self) -> None:
        super().__init__()
        self.calculator = Calculator()
        self.setWindowTitle("Qt Calculator")

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setPlaceholderText("Enter expression…")
        self.display.setFixedHeight(40)
        self.display.setStyleSheet("font-size: 18px; padding: 6px;")
        self.display.returnPressed.connect(self._evaluate)

        buttons_layout = self._create_buttons()
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        self.display.setFocus()

    def _create_buttons(self) -> QGridLayout:
        grid = QGridLayout()
        grid.setSpacing(6)

        for text, row, column in self.button_order:
            button = QPushButton(text)
            button.setFixedHeight(50)
            button.setStyleSheet("font-size: 16px;")
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            if text == "=":
                grid.addWidget(button, row, column, 1, 4)
                button.clicked.connect(self._evaluate)
            else:
                grid.addWidget(button, row, column)
                button.clicked.connect(lambda checked=False, value=text: self._handle_input(value))

        return grid

    def _handle_input(self, value: str) -> None:
        if value == "C":
            self.display.clear()
            return

        if value == "⌫":
            self.display.setText(self.display.text()[:-1])
            return

        self.display.setText(self.display.text() + value)

    def _evaluate(self) -> None:
        expression = self.display.text().strip()
        if not expression:
            return

        try:
            result = self.calculator.calculate(expression)
        except CalculatorError as error:
            QMessageBox.critical(self, "Error", str(error))
            return

        self.display.setText(str(result))


def run() -> None:
    """Launch the Qt calculator application."""

    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.resize(260, 360)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
