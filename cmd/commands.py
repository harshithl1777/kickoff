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
from controllers import basic, records, optimization

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
    if season is not None:
        errors.validate_season(season)
        errors.validate_team_in_season(league, team, season)
    winrate_percent = round(basic.overall_winrate(league, team, season), 2)

    if season is None:
        display_str = f"{team}'s winrate across all Premier League seasons is {winrate_percent}%."
    else:
        display_str = f"{team}'s winrate in the {season} season is {winrate_percent}%."

    io.info(message=display_str, color="dodger_blue1")


@app.command()
def teamvsleague(team: str = typer.Option(...), season: str = typer.Option(..., help="ex. 2009-10")) -> None:
    """Outputs various team statistics compared to the overall league statistics for the specified season.

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    errors.validate_team(league, team)
    errors.validate_season(season)

    data = [
        (
            "Average Goals Scored",
            round(basic.get_team_goals_scored(league, team, season), 2),
            round(basic.get_season_goals_scored(league, season), 2),
        ),
        (
            "Average Shot Accuracy (%)",
            round(basic.get_team_shot_accuracy(league, team, season), 2),
            round(basic.get_season_shot_accuracy(league, season), 2),
        ),
        (
            "Average Fouls Committed",
            round(basic.get_team_fouls(league, team, season), 2),
            round(basic.get_season_fouls(league, season), 2),
        ),
        (
            "Average Card Offenses",
            round(basic.get_team_cards(league, team, season), 2),
            round(basic.get_season_cards(league, season), 2),
        ),
    ]

    title = f"{team} Statistics Compared to the Rest of the League in the {season} Premier League Season"
    io.table(
        title=title,
        headers=["Statistic", f"{team}", "League"],
        colors=["cyan", "magenta", "cyan"],
        data=data,
        width=70,
    )


@app.command()
def streaks(
    season: str = typer.Option(..., help="ex. 2009-10"),
    topx: int = typer.Option(default=4, help="Enter the top x values to output"),
) -> None:
    """Outputs the longest win streaks statistic for the specified season.

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - 0 < topx <= 20
    """
    errors.validate_season(season)
    errors.validate_topx(topx, 20)

    highest_streaks = records.highest_win_streaks(league, season, topx)
    io.table(
        title=f"Highest Win Streaks in the {season} Premier League",
        headers=["Team", "Streak Length"],
        colors=["cyan", "magenta"],
        data=highest_streaks,
        width=70,
    )


@app.command()
def comebacks(
    season: str = typer.Option(default=None, help="ex. 2009-10"),
    topx: int = typer.Option(default=4, help="Enter the top x values to output"),
) -> None:
    """Outputs the winrate statistic for the specified team & season.
    If no arguments are found, the statistic will be calculated for all teams and seasons.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    best_comebacks = records.best_comebacks(league, season, topx)

    if season is None:
        errors.validate_topx(topx, 100)
        title = "Most Clutch Teams in the Premier League"
    else:
        errors.validate_season(season)
        errors.validate_topx(topx, 20)
        title = f"Most Clutch Teams in the {season} Premier League Season"

    io.table(
        title=title,
        headers=["Team", "Half-Time Score", "Full-Time Score", "Comeback Size"],
        colors=["cyan", "magenta", "yellow", "green"],
        data=best_comebacks,
        width=100,
    )


@app.command()
def goals(
    season: str = typer.Option(default=None, help="ex. 2009-10"),
    topx: int = typer.Option(default=4, help="Enter the top x values to output"),
) -> None:
    """Outputs the winrate statistic for the specified team & season.
    If no arguments are found, the statistic will be calculated for all teams and seasons.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - topx > 0
        - season is not None and topx <= 100
        - season is None and topx <= 20
    """
    if season is not None:
        errors.validate_season(season)
        errors.validate_topx(topx, 20)
    else:
        errors.validate_topx(topx, 100)

    most_goals = records.most_goals_scored(league, season, topx)
    if season is None:
        title = "Most Goals Scored in the Premier League"
    else:
        title = f"Most Goals Scored in the {season} Premier League"
    io.table(
        title=title, headers=["Team", "Most Goals In a Game"], colors=["cyan", "magenta"], data=most_goals, width=70
    )


@app.command()
def improvement(
    season: str = typer.Option(..., help="ex. 2009-10"),
    topx: int = typer.Option(default=4, help="Enter the top x values to output"),
) -> None:
    """Output the topx most improved teams in the season.

    Preconditions
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    errors.validate_season(season)
    errors.validate_topx(topx, 20)

    most_improved = records.most_improved_teams(league, season, topx)
    title = f"Most Improved Teams in the {season} Premier League Season"
    io.table(
        title=title,
        headers=["Team", "Lowest Win (%)", "Final Winrate (%)", "Winrate Improvement (%)"],
        colors=["cyan", "magenta", "cyan", "magenta"],
        data=most_improved,
        width=80,
    )


@app.command()
def optimalfouls(
    team: str = typer.Option(default=None),
    topx: int = typer.Option(default=4, help="Enter the top x values to output"),
) -> None:
    """Outputs the optimal fouls for the provided team.

    Preconditions
        - team is a valid team
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - 0 < topx <= 7
    """
    if team is not None:
        errors.validate_team(league, team)
    errors.validate_topx(topx, 7)
    optimal_fouls = optimization.calculate_optimal_fouls(league, team, topx)

    if team is None:
        title = "Optimal Foul Ranges for all Premier League Teams"
    else:
        title = f"Optimal Foul Ranges for {team}"
    io.table(
        title=title,
        headers=["Foul Range", "Number of Wins Recorded", "Percent of Total Decade Wins"],
        colors=["cyan", "magenta", "green"],
        data=optimal_fouls,
        width=90,
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
