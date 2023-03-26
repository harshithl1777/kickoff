"""Module containing the Team class and other related components"""

from __future__ import annotations
from dataclasses import dataclass


from match import Match

@dataclass
class Team:
    """A football team playing in a particular season of the Premier League.

    Instance Attributes:
        - name: The name of this team.
        - matches: A chronologically ordered list of the matches played by this team in the season.

    Representation Invariants:
        ...
    """
    name: str
    matches: list[Match]
    