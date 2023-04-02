"""Kickoff Project: controllers / records.py

This module contains functionality for finding various records in the datasets.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""
# pylint: disable=C0200

from typing import Optional
from models.league import League


def most_goals_scored(league: League, season: Optional[str] = None, topx: int = 4) -> list[tuple[str, int]]:
    """Return a list of the topx teams that scored the most goals in the whole league

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - 0 < topx <= 20
    """
    matches = []
    season_orders = set()
    teams = league.get_team_names()
    for team in teams:
        team_matches = league.get_team(team).matches
        for match in team_matches:
            identifier = str(match.order) + match.season
            if identifier not in season_orders:
                matches.append(match)
                season_orders.add(identifier)
    goals = []

    for match in matches:
        if season is None or match.season == season:
            if match.result is None:
                winner_goals = match.details[match.home_team.name].full_time_goals
                team_name = str(match.home_team.name) + " & " + str(match.away_team.name)
            else:
                winner_goals = match.details[match.result.name].full_time_goals
                team_name = match.result.name

            if season is None:
                team_name += f" ({match.season})"

            goals.append((team_name, winner_goals))
    return sorted(goals, key=lambda goal: goal[1], reverse=True)[:topx]


def highest_win_streaks(league: League, season: str, topx: int = 4) -> list[tuple[str, int]]:
    """Return a list of the topx highest win streaks in the specified season

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - topx > 0
        - season is not None and topx <= 100
        - season is None and topx <= 20
    """
    team_names = league.get_team_names(season)
    streaks = []
    for name in team_names:
        team = league.get_team(name)
        matches = team.matches

        highest_streak = 0
        current_streak = 0
        for i in range(len(matches)):
            if matches[i].season == season:
                if matches[i].result == team:
                    current_streak += 1
                    if i == len(matches) - 1 and current_streak > highest_streak:
                        highest_streak = current_streak
                elif highest_streak < current_streak:
                    highest_streak = current_streak
                    current_streak = 0

        streaks.append((name, highest_streak))
    return sorted(streaks, key=lambda streak: streak[1], reverse=True)[:topx]
