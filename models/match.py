"""Module containing the Match class and other related components"""

from __future__ import annotations
from datetime import datetime
from dataclasses import dataclass
from typing import Literal
from python_ta.contracts import check_contracts

import team


@check_contracts
@dataclass
class Match:
    """A Premier League match between two teams in a particular season.

        Instance Attributes:
            - home_team: The team playing at its home ground in this match.
            - away_team: The team playing away from its home ground in this match.
            - date_time: The date and time of the match played.
            - winner: The name of the winning team of the match, or None if the match ended in a draw.
            - details: A mapping from each team name to its corresponding match details.

        Representation Invariants:
            - len(teams) == 2
            - self.season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
            '2017-18', '2018-19']
    """

    season: str
    away_team: team.Team
    home_team: team.Team
    date_time: datetime
    details: dict[team.Team, MatchDetails]
    result: Literal["HOME_WIN", "AWAY_WIN", "DRAW"]


@check_contracts
@dataclass
class MatchDetails:
    """The details of a team's performance in a Premier League match.

    Instance Attributes:
        - team: The team this MatchDetails refers to
        - fouls: number of fouls commited by the team in the match
        - shots: number of shots taken by the team in the match
        - shots_on_target: number of shots that were on target by the team in the match
        - red_cards: number of red cards given to the team in the match
        - yellow_cards: number of yellow cards given to the team in the match
        - half_time_goals: number of goals scored by the team at half time
        - full_time_goals: number of goals scored by the team at full time

    Representation Invariants:
        ...
    """

    team: team.Team
    fouls: int
    shots: int
    shots_on_target: int
    red_cards: int
    yellow_cards: int
    half_time_goals: int
    full_time_goals: int


if __name__ == "__main__":
    import python_ta

    python_ta.check_all()
