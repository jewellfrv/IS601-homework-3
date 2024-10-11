import sys
from App.Commands import Command


class SubtractCommand(Command):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a - self.b
        print(f"The result of subtracting {self.b} from {self.a} is {result}")
