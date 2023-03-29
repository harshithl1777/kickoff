"""Kickoff Project: models / league.py

This module contains the League class and other related components.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from models.team import Team
from models.match import Match


class League:
    """A graph-based representation of Premier League matches and teams.

    Instance Attributes:
        - teams:
            A mapping containing the teams playing in this season.
            Each key is the name of the team
            and the corresponding values are the Team object corresponding to the team.
        - matches:
            A chronologically ordered list of all matches played in this season.

    Representation Invariants:
        - all({ name == self.teams[name].name for name in self.teams })
        - len(self.matches) > 0
    """

    teams: dict[str, Team] = {}
    matches: list[Match] = []


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["team", "match"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
