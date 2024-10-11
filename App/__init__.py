from App.Commands import CommandHandler
from App.Commands.Add import AddCommand
from App.Commands.Subtract import SubtractCommand
from App.Commands.Multiply import MultiplyCommand
from App.Commands.Divide import DivideCommand


class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        self.command_handler.register_command("Add", AddCommand())
        self.command_handler.register_command("Subtract", SubtractCommand())
        self.command_handler.register_command("Multiply", MultiplyCommand())
        self.command_handler.register_command("Divide", DivideCommand())
        
        print("Type 'Add' to Add")
        while True:  #REPL
            self.command_handler.execute_command(input(">>> ").strip())
