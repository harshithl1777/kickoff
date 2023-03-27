"""Module containing the Match class and other related components"""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
from dataclasses import dataclass

import team


@dataclass
class Match:
    """A Premier League match between two teams in a particular season.

    Instance Attributes:
        - home_team: The team playing at its home ground in this match.
        - away_team: The team playing away from its home ground in this match.
        - date_time: The date and time of the match played.
        - winner: The name of the winning team of the match, or None if the match ended in a draw.
        - details: A mapping from each team name to its corresponding match details.

    Representation Invariants:
        - len(teams) == 2   
    """
    away_team: team.Team
    home_team: team.Team
    date_time: datetime
    details: dict[str, MatchDetails]
    result: MatchResult


@dataclass
class MatchDetails:
    """The details of a team's performance in a Premier League match.

    Instance Attributes:
        - team: The team this MatchDetails refers to.
        - fouls_commited: number of fouls commited by the team in the match
        - red_cards: number of red cards given to the team in the match
        - yellow_cards: number of yellow cards given to the team in the match
        - offsides: number of offsides awarded to the team in the match 
        - half_time_goals: number of goals scored by the team at half time
        - full_time_goals: number of goals scored by the team at full time

    Representation Invariants:
        ...
    """
    team: team.Team
    fouls_commited: int
    red_cards: int
    yellow_cards: int
    offsides: int
    half_time_goals: int
    full_time_goals: int


MatchResult = Enum("MatchResult", ["HOME_WIN", "AWAY_TEAM", "DRAW"])
