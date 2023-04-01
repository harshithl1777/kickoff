"""Kickoff Project: cmd / output.py

This module contains helper functions to output various messages to the console using rich.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""
# pylint: disable=C0200

from typing import Any
from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich import box
import typer


def info(message: str, color: str) -> None:
    """Uses rich to print a colored information message."""
    console = Console()
    console.line()
    console.print(message, style=color)


def error(message: str) -> None:
    """Uses rich to print a colored error message."""
    console = Console()
    console.line()
    error_message = "Error: " + message
    console.print(error_message, style="red")
    raise typer.Exit()


def table(title: str, headers: list[str], colors: list[str], data: list[tuple[Any]], width: int) -> None:
    """Uses rich to print a table with the specified table, headers, colors and data.

    Preconditions:
        - len({len(headers), len(colors), len(data[0])}) == 1
        - len({len(row) for row in data}) == 1
    """
    title_style = Style(bold=True)
    table = Table(title=title, width=width, box=box.HORIZONTALS, show_footer=False, title_style=title_style)

    for i in range(len(headers)):
        table.add_column(headers[i], style=colors[i])

    for row in data:
        renderable_row = [str(cell) for cell in row]
        table.add_row(*renderable_row)

    console = Console()
    console.line()
    console.print(table)


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["rich.console"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
