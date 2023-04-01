"""Kickoff Project: controllers / records.py

This module contains functionality for finding various records in the datasets.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from models.team import Team
from models.league import League


def highest_win_loss_streaks(league: League, season: str) -> dict[str, list[tuple[Team, int]]]:
    """Return a dictionary of the highest win and loss streaks in the specified season"""
    raise NotImplementedError 