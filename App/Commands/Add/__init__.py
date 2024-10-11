import sys
from app.commands import Command


class AddCommand(Command):
    def execute(self):
        sys.exit("Add")
