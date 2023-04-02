"""Kickoff Project: cmd / commands.py

This module sets up various CLI commands that the user can use to interact with our application. 
It simply parses user commands and ensures that inputs are acceptable and delegates the actual functionality 
to other functions / classes.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

import cmd.output as io
import cmd.errors as errors
from typing import Optional
import typer

from utils import constants, data
from controllers import basic, records

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
        - If season is specified, team must have played a match in the season
    """
    errors.validate_team(league, team)
    errors.validate_season(season)
    errors.validate_team_in_season(league, team, season)
    winrate_percent = round(basic.overall_winrate(league, team, season), 2)

    if season is None:
        display_str = f"{team}'s winrate across all Premier League seasons is {winrate_percent}%."
    else:
        display_str = f"{team}'s winrate in the {season} season is {winrate_percent}%."

    io.info(message=display_str, color="dodger_blue1")


@app.command()
def streaks(season: str = typer.Option(..., help="ex. 2009-10")) -> None:
    """Outputs the longest win streaks statistic for the specified season.

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    errors.validate_season(season)

    highest_streaks = records.highest_win_streaks(league, season)
    io.table(
        title=f"Highest Win Streaks in the {season} Premier League",
        headers=["Team", "Streak Length"],
        colors=["cyan", "magenta"],
        data=highest_streaks,
        width=70,
    )


@app.command()
def goals(season: str = typer.Option(default=None, help="ex. 2009-10")) -> None:
    """Outputs the winrate statistic for the specified team & season.
    If no arguments are found, the statistic will be calculated for all teams and seasons.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    most_goals = records.most_goals_scored(league, season)
    if season is None:
        title = "Most Goals Scored in the Premier League"
    else:
        title = f"Most Goals Scored in the {season} Premier League"
    io.table(
        title=title, headers=["Team", "Most Goals In a Game"], colors=["cyan", "magenta"], data=most_goals, width=70
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
