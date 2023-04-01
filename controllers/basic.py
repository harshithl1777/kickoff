"""Kickoff Project: controllers / basic.py

This module contains functionality for performing basic analysis on the premier league data.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from typing import Optional

from models.league import League


def overall_winrate(league: League, team_name: str, season: Optional[str] = None) -> float:
    """Return the overall winrate of the Team with team_name in the League.
    Only consider matches in the season if the season is provided.

    Raise a ValueError if the team did not take part in the season.

    Preconditons:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in self._teams
    """
    total_matches = 0
    total_wins = 0

    team = league.get_team(team_name)
    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        if match.result == team:
            total_wins += 1

    if total_matches == 0:
        raise ValueError("team did not play in season")

    return total_wins / total_matches


def get_team_goals_scored(league: League, team_name: str, season: Optional[str] = None):
    """Return the average number of goals scored by a team in their matches.
    Consider the matches in a specific season if it is provided.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in self._teams
    """
    total_matches = 0
    goals_scored = 0
    team = league.get_team(team_name)

    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        goals_scored += match.details[team_name].full_time_goals

    if total_matches == 0:
        raise ValueError("team did not play in season")

    return goals_scored / total_matches


def get_team_yellow_cards(league: League, team_name: str, season: Optional[str] = None):
    """Return the average number of yellow cards received by a team in their matches.
    Consider the matches in a specific season if it is provided.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in self._teams
    """
    total_matches = 0
    yellow_cards = 0
    team = league.get_team(team_name)

    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        yellow_cards += match.details[team_name].yellow_cards

    if total_matches == 0:
        raise ValueError("team did not play in season")

    return yellow_cards / total_matches


def get_team_red_cards(league: League, team_name: str, season: Optional[str] = None):
    """Return the average number of red cards received by a team in their matches.
    Consider the matches in a specific season if it is provided.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in self._teams
    """
    total_matches = 0
    red_cards = 0
    team = league.get_team(team_name)

    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        red_cards += match.details[team_name].red_cards

    if total_matches == 0:
        raise ValueError("team did not play in season")

    return red_cards / total_matches


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["typing", "models.league"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
