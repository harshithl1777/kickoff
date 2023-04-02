"""Kickoff Project: controllers / records.py

This module contains functionality for finding various records in the datasets.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from models.team import Team
from models.league import League
from typing import Optional


def highest_win_loss_streaks(league: League, season: str) -> dict[str, list[tuple[Team, int]]]:
    """Return a dictionary of the highest win and loss streaks in the specified season"""
    raise NotImplementedError 

def most_goals_scored(league: League, season: Optional[str] = None) -> list[tuple[str, int]]:
    """Return a list of the teams that scored the most goals in the whole league"""
    
    matches = []

    for val in league._teams:
        matches.append(league._teams[val].matches)

    if season is None:
        max_goals = 0
        final = []

        for match in matches:
            if match.full_time_goals >= max_goals:
                final.insert(((match.team.name, match.full_time_goals)), 0)
            
            max_goals += 1
        
        return final[:4]
   
    else:
        max_goals = 0
        final = []

        for match in matches:
            if match.season == season:
                if match.full_time_goals >= max_goals:
                    final.insert(((match.team.name, match.full_time_goals)), 0)
                
                max_goals += 1
            
            return final[:4]
