import sys
from App.Commands import Command


class MultiplyCommand:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self) -> float:
        return self.a * self.b
