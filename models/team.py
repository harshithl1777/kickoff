"""Module containing the Team class and other related components"""

from dataclasses import dataclass

@dataclass
class Team:
    """A football team in the premier league.

    Instance Attributes:
        - name: the name of this team

    Representation Invariants:
        ...
    """
    name: str
    