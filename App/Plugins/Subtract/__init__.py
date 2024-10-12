import sys
from App.Commands import Command


class SubtractCommand(Command):
    def execute(self, a, b):
        result = a - b
        print(result)  # Ensure it prints the result
        return result
