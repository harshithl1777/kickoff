"""Module containing the Season class and other related components"""

from enum import Enum

from team import Team
from match import Match


class PremierLeague:
    """A graph-based representation of Premier League matches and teams.

    Instance Attributes:
        - teams: 
            A mapping containing the teams playing in this season.
            Each key is the name of the team
            and the corresponding values are the Team object corresponding to the team. 
        - matches:
            A chronologically ordered list of all matches played in this season.

    Representation Invariants:
        ...
    """
    teams: dict[str, Team]
    matches: list[Match]


"""
All Premier League seasons in the dataset.
Season.ABCD corresponds to the 20AB - 20CD season.
"""
Seasons = Enum("Seasons",
               ["0910",
                "1011",
                "1112",
                "1213",
                "1314"
                "1415",
                "1516",
                "1617",
                "1718",
                "1819"]
               )
