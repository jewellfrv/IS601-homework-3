from app.Commands import CommandHandler
from app.Commands.Add import AddCommand
from app.Commands.Subtract import SubtractCommand
from app.Commands.Multiply import MultiplyCommand
from app.Commands.Divide import DivideCommand


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
