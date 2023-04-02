"""Kickoff Project: utils / league.py

This module contains helper functions for the League class.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""
from models.match import Match


def get_all_matches(league) -> list[Match]:
    """Return a list of all the matches in the entire League class"""
    matches = []

    teams = league.get_team_names()
    for team in teams:
        team_matches = league.get_team(team).matches
        for match in team_matches:
            if match not in matches:
                matches.append(match)

    return matches
