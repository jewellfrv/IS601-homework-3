from abc import ABC, abstractmethod
from typing import Type

class Command(ABC):
    """Abstract base class for all commands."""

    @abstractmethod
    def execute(self):
        """Abstract method that needs to be implemented by all concrete command classes."""
        pass


class CommandHandler:
    """Handles the registration and execution of commands."""

    def __init__(self):
        """Initialize with an empty dictionary of commands."""
        self.commands = {}

    def register_command(self, command_name: str, command: Type[Command]):
        """
        Register a command with the command handler.

        Args:
            command_name (str): The name of the command.
            command (Type[Command]): The class of the command to be registered.
        """
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """
        Execute a command based on the command name.

        Args:
            command_name (str): The name of the command to be executed.

        Raises:
            KeyError: If the command is not found in the registered commands.
        """
        # Easier to ask for forgiveness than permission (EAFP)
        try:
            command_instance = self.commands[command_name]()  # Instantiate the command
            command_instance.execute()  # Call the execute method
        except KeyError:
            print(f"No such command: {command_name}")
        except Exception as e:
            print(f"An error occurred while executing the command: {e}")
            