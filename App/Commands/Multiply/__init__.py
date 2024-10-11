import sys
from App.Commands import Command


class MultiplyCommand(Command):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a * self.b
        print(f"The result of multiplying {self.a} and {self.b} is {result}")
