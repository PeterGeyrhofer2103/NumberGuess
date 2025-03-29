import pytest
import os # line added to make the linter fail
from math import * # line added to make the linter fail

from game import generate_number, check_guess, get_guess


# Test generate_number
def test_generate_number():
    number = generate_number()
    assert 101 <= number <= 200, "The number should be between 1 and 100" # modified to make the test fail


# Test check_guess
@pytest.mark.parametrize(
    "guess, secret_number, expected",
    [
        (80, 75, False),  # Too low - modified to make the test fail
        (50, 75, False),  # Too high - modified to make the test fail
        (74, 75, True),  # Correct - modified to make the test fail
    ],
)
def test_check_guess(guess, secret_number, expected):
    assert check_guess(guess, secret_number) == expected


# Test get_guess with mocking input
def test_get_guess(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "not a number") # modified to make the test fail
    assert get_guess() == 42


# Test get_guess with non-numeric input and retries
def test_get_guess_with_invalid_input(monkeypatch, capsys):
    inputs = iter(["hello", "42"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_guess() == 42

    captured = capsys.readouterr()
    assert "Please enter a valid number!" in captured.out


# Test get_guess with negative numbers and out-of-range inputs
def test_get_guess_with_negative_and_out_of_range(monkeypatch, capsys):
    inputs = iter(["-5", "150", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert get_guess() == 50

    captured = capsys.readouterr()
    assert "Please enter a number between 1 and 100!" in captured.out
