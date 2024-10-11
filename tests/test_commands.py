import pytest
from App import App
from App.Commands.Add import AddCommand
from App.Commands.Subtract import SubtractCommand
from App.Commands.Multiply import MultiplyCommand
from App.Commands.Divide import DivideCommand

def test_Add_command(capfd):
    command = AddCommand()
    command.execute(4, 5) #Add two numbers for addition
    out, err = capfd.readouterr()
    assert out == "9\n", "The AddCommand should print the sum of the numbers"

def test_Subtract_command(capfd):
    command = SubtractCommand()
    command.execute(9, 5)
    out, err = capfd.readouterr()
    assert out == "4\n", "The SubtractCommand should print the sum of the numbers'"

def test_App_Multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command."""
    # Simulate user entering 'multiply' followed by 'exit'
    inputs = iter(['multiply', '5', '4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is a method that handles commands

    # Verify that the output contains the expected result of the multiplication
    out, err = capfd.readouterr()
    assert "The result of multiplying 5 and 4 is 20" in out, "The MultiplyCommand did not produce the expected output"
    
    # Check that the app exits correctly
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_App_Divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'divide' command."""
    # Simulate user entering 'divide' followed by two numbers and then 'exit'
    inputs = iter(['divide', '10', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is a method that handles commands

    # Verify that the output contains the expected result of the division
    out, err = capfd.readouterr()
    assert "The result of dividing 10 by 2 is 5.0" in out, "The DivideCommand did not produce the expected output"
    
    # Check that the app exits correctly
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
