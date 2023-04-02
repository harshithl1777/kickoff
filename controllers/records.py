"""Kickoff Project: controllers / records.py

This module contains functionality for finding various records in the datasets.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""
# pylint: disable=C0200

from models.league import League
from typing import Optional

def most_goals_scored(league: League, season: Optional[str] = None) -> list[tuple[str, int]]:
    """Return a list of the teams that scored the most goals in the whole league"""
    
    matches = []
    teams = league.get_team_names()
    for team in teams:
        matches.extend(league.get_team(team).matches)

    max_goals = 0
    final = []

    for match in matches:
        if season is None or match.season == season:
            if match.result is None:
                winner_goals = match.details[match.home_team.name].full_time_goals
            else:
                winner_goals = match.details[match.result.name].full_time_goals
            if winner_goals >= max_goals:
                max_goals = winner_goals
                final.insert(((match.result.name, winner_goals)), 0)
    return final[:4]
        
def highest_win_streaks(league: League, season: str) -> list[tuple[str, int]]:
    """Return a dictionary of the highest win streaks in the specified season

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
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
    return sorted(streaks, key=lambda streak: streak[1], reverse=True)[:4]
