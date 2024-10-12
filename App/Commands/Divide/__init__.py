import sys
from App.Commands import Command


class DivideCommand:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self) -> float:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b
