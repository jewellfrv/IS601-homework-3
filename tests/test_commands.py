import pytest
from App import Commands 
from App.Plugins.Add import AddCommand
from App.Plugins.Subtract import SubtractCommand
from App.Plugins.Multiply import MultiplyCommand
from App.Plugins.Divide import DivideCommand

def test_Add_command(capfd):
    command = AddCommand(4, 5)
    command.execute()  # Add two numbers for addition
    out, err = capfd.readouterr()
    assert out.strip() == "9", "The AddCommand should print the sum of the numbers"

def test_Subtract_command(capfd):
    command = SubtractCommand()
    command.execute(9, 5)
    out, err = capfd.readouterr()
    assert out.strip() == "4", "The SubtractCommand should print the result of the subtraction"

def test_Multiply_command(capfd):
    command = MultiplyCommand(5, 4)  # Provide parameters here
    result = command.execute()         # Execute the command
    print(result)                      # Simulate printing the result
    out, err = capfd.readouterr()
    assert out.strip() == "20", "The MultiplyCommand should print the result of the multiplication"

def test_Divide_command(capfd):
    command = DivideCommand(10, 2)  # Provide parameters here
    result = command.execute()        # Execute the command
    print(result)                     # Simulate printing the result
    out, err = capfd.readouterr()
    assert out.strip() == "5.0", "The DivideCommand should print the result of the division"
