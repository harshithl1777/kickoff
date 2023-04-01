"""Kickoff Project: cmd / output.py

This module contains helper functions to output various messages to the console using rich.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from rich.console import Console


def print_error(message: str) -> None:
    """Uses rich to print a colored error message"""
    console = Console()
    error = "Error: " + message
    console.print(error, style="red")


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["rich.console"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
