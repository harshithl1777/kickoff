"""Kickoff Project: models / basic.py

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

    team = league._teams[team_name]
    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        if match.result == team:
            total_wins += 1

    if total_matches == 0:
        raise ValueError('team did not play in season')

    return total_wins / total_matches
