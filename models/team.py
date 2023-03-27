"""Module containing the Team class and other related components"""

from __future__ import annotations
from dataclasses import dataclass


from match import Match
import premier_league

@dataclass
class Team:
    """A football team playing in a particular season of the Premier League.

    Instance Attributes:
        - name: The name of this team.
        - matches: A chronologically ordered list of the matches played by this team in the season.
        - seasons: The seasons this team has participated in.

    Representation Invariants:
        ...
    """
    name: str
    matches: list[Match]
    seasons: list[premier_league.Seasons]
    