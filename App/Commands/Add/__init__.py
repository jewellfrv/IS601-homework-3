import sys
from App.Commands import Command

class AddCommand(Command):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a + self.b
        return self.a + self.b
