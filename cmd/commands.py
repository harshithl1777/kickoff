"""Kickoff Project: cmd / commands.py

This module sets up various CLI commands that the user can use to interact with our application. 
It simply parses user commands and ensures that inputs are acceptable and delegates the actual functionality 
to other functions / classes.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

import cmd.output as io
import typer

from utils import constants, data
from controllers import basic, optimization, records

constants = constants.Constants()
app = typer.Typer(help=constants.retrieve("HELP_COMMAND_INTRO"))
league = data.load_csv_files()


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


@app.command()
def streaks(season: str = typer.Option(..., help="ex. 2009-10")) -> None:
    """Outputs the longest win streaks statistic for the specified season.

    Preconditions
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    highest_streaks = records.highest_win_streaks(league, season)
    io.output_table(
        title=f"Highest Win Streaks in the {season} Premier League",
        headers=["Team", "Streak Length"],
        colors=["cyan", "magenta"],
        data=highest_streaks,
        width=70,
    )


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["typer", "utils.constants"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
