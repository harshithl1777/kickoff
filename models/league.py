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

    _teams: dict[str, Team]

    def __init__(self) -> None:
        self._teams = {}

    def add_team(self, name: str) -> Team:
        """Add a new team with the given team name to this league and return it.

        Preconditions
            - name not in self._teams
        """
        team = Team(name=name, matches=[])
        self._teams[name] = team
        return team

    def add_match(self, team1: str, team2: str, match: Match) -> None:
        """Add a new match between the two given teams.
        Add each team to the league if they have not been added already.

        Preconditions
            - team1 in {match.away_team.name, match.home_team.name}
            - team2 in {match.away_team.name, match.home_team.name}
            - team1 != team2
        """
        if team1 not in self._teams:
            self.add_team(team1)
        if team2 not in self._teams:
            self.add_team(team2)

        self._teams[team1].matches.append(match)
        self._teams[team2].matches.append(match)

    def team_in_league(self, name: str) -> bool:
        """Check if the given team exists within this league by the given name"""
        return name in self._teams

    def get_team(self, name: str) -> Team:
        """Retrieve a specific team object based on the given name

        Preconditions
            - name in self._teams
        """
        return self._teams[name]


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["team", "match"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
