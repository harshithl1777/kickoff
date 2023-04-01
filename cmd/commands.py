"""Kickoff Project: cmd / commands.py

This module sets up various CLI commands that the user can use to interact with our application. 
It simply parses user commands and ensures that inputs are acceptable and delegates the actual functionality 
to other functions / classes.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

import typer
from typing import Optional
from rich.console import Console

from utils import constants, data
from controllers import basic, optimization, records

league = data.load_csv_files()
constants = constants.Constants()
app = typer.Typer(help=constants.retrieve("HELP_COMMAND_INTRO"))


@app.command()
def winrate(
    team: str = typer.Option(...), season: Optional[str] = typer.Option(default=None, help="ex. 2009-10")
) -> None:
    """Outputs the winrate percent of the specified team.
    If season is specified, the winrate will be calculated only for the season.

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

    console.print(display_str)


@app.command()
def streaks(season: str = typer.Option(..., help="ex. 2009-10")) -> None:
    """Outputs the longest win & loss streaks statistic for the specified season.

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    raise NotImplementedError


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["typer", "utils.constants"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
