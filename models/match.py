"""Module containing the Match class and other related components"""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
from dataclasses import dataclass

from team import Team


@dataclass
class Match:
    """A premier league match between two teams in a particular season.

    Instance Attributes:
        - teams: a set of the the two teams that played this match
        - date_time: the date and time of the match played
        - winner: the winner of the match, or None if the match ended in a draw
        - details: a dictionary mapping each teams to its corresponding match details

    Representation Invariants:
        - len(teams) == 2
    """
    teams: set[Team]
    date_time: datetime
    details: dict[Team, MatchDetails]
    winner: Optional[Team]



@dataclass
class MatchDetails:
    """The details of a team's performance in a Premier League match.

    Instance Attributes:
        - fouls_commited: number of fouls commited by the team in the match
        - red_cards: number of red cards given to the team in the match
        - yellow_cards: number of yellow cards given to the team in the match
        - offsides: number of offsides awarded to the team in the match 
        - half_time_goals: number of goals scored by the team at half time
        - _timfulle_goals: number of goals scored by the team at full time

    Representation Invariants:
        ...
    """
    fouls_commited: int
    red_cards: int
    yellow_cards: int
    offsides: int
    half_time_goals: int
    full_time_goals: int
    