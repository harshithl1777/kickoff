"""Kickoff Project: cmd / commands.py

This module sets up various CLI commands that the user can use to interact with our application. 
It simply parses user commands and ensures that inputs are acceptable and delegates the actual functionality 
to other functions / classes.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

import typer
from utils.constants import Constants

constants = Constants()
app = typer.Typer(help=constants.retrieve("HELP_COMMAND_INTRO"))


@app.command()
def full(
    team: str = typer.Option(default="ALL"), season: str = typer.Option(default="ALL", help="ex. 2009-10")
) -> None:
    """Outputs all statistics for the specified team & season.
    If no arguments are found, the statistic will be calculated for all teams and seasons.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    print("To be implemented!")


@app.command()
def winrate(
    team: str = typer.Option(default="ALL"), season: str = typer.Option(default="ALL", help="ex. 2009-10")
) -> None:
    """Outputs the winrate statistic for the specified team & season.
    If no arguments are found, the statistic will be calculated for all teams and seasons.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    raise NotImplementedError


if __name__ == "__main__":
    import python_ta

    python_ta.check_all()
