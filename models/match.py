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
        - goals: a list of tuples, where each tuple represents a goal and is of the form:
          (minute the goal was scored, team that scored the goal)   

    Representation Invariants:
        - len(teams) == 2
    """
    teams: set[Team]
    date_time: datetime
    goals: list[tuple[int, Team]]
    details: dict[Team, MatchDetails]
    winner: Optional[Team]



@dataclass
class MatchDetails:
    """The details of a team's performance in a Premier League match.

    Instance Attributes:
        - fouls_commited
        - red_cards
        - yellow_cards
        - offsides

    Representation Invariants:
        ...
    """
    fouls_commited: int
    red_cards: int
    yellow_cards: int
    offsides: int