"""Kickoff Project: cmd / commands.py

This module sets up various CLI commands that the user can use to interact with our application. 
It simply parses user commands and ensures that inputs are acceptable and delegates the actual functionality 
to other functions / classes.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

import typer
from utils.constants import Constants
from controllers import basic, records
from controllers.records import most_goals_scored
from typing import Optional
from rich.console import Console

from utils import constants, data

league = data.load_csv_files()
constants = constants.Constants()

constants = Constants()
app = typer.Typer(help=constants.retrieve("HELP_COMMAND_INTRO"))


@app.command()
def winrate(team: str = typer.Option(default="ALL"), season: str = typer.Option(default="ALL", help="ex. 2009-10")) -> None:
    """Outputs the winrate statistic for the specified team & season.
    If no arguments are found, the statistic will be calculated for all teams and seasons.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    console = Console()
    winrate = round(basic.overall_winrate(league, team, season), 2)

    if season is None:
        display_str = f"{team}'s winrate across all Premier League seasons is {winrate}%"
    else:
        display_str = f"{team}'s winrate in the {season} season is {winrate}%"

    console.print(display_str, style="blue")


@app.command()
def streaks(season: str = typer.Option(..., help="ex. 2009-10")) -> None:
    """Outputs the longest win & loss streaks statistic for the specified season.

    Preconditions
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    raise NotImplementedError

@app.command()
def goals(season: str = typer.Option(default=None, help="ex. 2009-10")) -> None:
    """Outputs the winrate statistic for the specified team & season.
    If no arguments are found, the statistic will be calculated for all teams and seasons.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    console = Console()
    most_goals = most_goals_scored(league, season)


    display_str = f"most goals across all Premier League seasons is {most_goals}%"

    console.print(display_str, style="blue")

if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["typer", "utils.constants"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
