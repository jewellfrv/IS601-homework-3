from App.Commands import CommandHandler
from App.Commands.Add import AddCommand
from App.Commands.Subtract import SubtractCommand
from App.Commands.Multiply import MultiplyCommand
from App.Commands.Divide import DivideCommand


def start(self):
    # Register commands here (pass class references, not instances)
    self.command_handler.register_command("Add", AddCommand)
    self.command_handler.register_command("Subtract", SubtractCommand)
    self.command_handler.register_command("Multiply", MultiplyCommand)
    self.command_handler.register_command("Divide", DivideCommand)
    
    print("Type 'Add' to Add")
    
    while True:  # REPL
        command_name = input(">>> ").strip()
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        self.command_handler.execute_command(command_name, a, b)
