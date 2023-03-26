"""Module containing the Season class and other related components"""


from team import Team
from match import Match


class Season:
    """A graph-based representation of a Premier League season.


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
