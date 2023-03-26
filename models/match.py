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
        - home_team: The team playing the match at home. 
        - away_team: The team playing the match away from their home ground. 
        - date_time: The date and time of the match played.
        - details: A mapping from each team name to its corresponding match details.
        - result: the result of this match.

    Representation Invariants:
        - len(details) == 2
        - home_team.name in details
        - away_team.name in details
    """
    home_team: team.Team
    away_team: team.Team
    date_time: datetime
    details: dict[str, MatchDetails]
    result: MatchResult


@dataclass
class MatchDetails:
    """The details of a team's performance in a Premier League match.

    Instance Attributes:
        - match: The match that this match detail refers to.
        - team: The team that these details are about.
        - fouls_commited: number of fouls commited by the team in the match.
        - red_cards: number of red cards given to the team in the match.
        - yellow_cards: number of yellow cards given to the team in the match.
        - offsides: number of offsides awarded to the team in the match.
        - half_time_goals: number of goals scored by the team at half time.
        - full_time_goals: number of goals scored by the team at full time.

    Representation Invariants:
        ...
    """
    match: Match
    team: team.Team
    fouls_commited: int
    red_cards: int
    yellow_cards: int
    offsides: int
    half_time_goals: int
    full_time_goals: int


MatchResult = Enum('MatchResult', ['HOME_WIN', 'AWAY_WIN', 'DRAW'])
