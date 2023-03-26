"""Module containing the Team class and other related components"""

from dataclasses import dataclass

from match import Match

@dataclass
class Team:
    """A football team in the Premier League in a particular season.

    Instance Attributes:
        - name: the name of this team
        - matches: a chronological list of the matches played by this team in the season

    Representation Invariants:
        ...
    """
    name: str
    matches: list[Match]