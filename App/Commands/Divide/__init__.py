import sys
from App.Commands import Command


class DivideCommand(Command):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = self.a / self.b
            print(f"The result of dividing {self.a} by {self.b} is {result}")
