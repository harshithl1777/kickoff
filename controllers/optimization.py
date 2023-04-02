"""Kickoff Project: controllers / records.py

This module contains functionality for finding various records in the datasets.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""
# pylint: disable=C0206
from models.league import League
from utils.league import get_all_matches


def calculate_optimal_fouls(league: League, team: str = None, topx: int = 4) -> list[tuple[str, float]]:
    """Returns a list of the topx optimal foul ranges and the % of wins they account for

    Preconditions
        - team is a valid team
        - 0 < topx <= 7
    """
    if team is None:
        matches = get_all_matches(league)
    else:
        matches = league.get_team(team).matches

    foul_wins = {}
    for match in matches:
        if match.result is not None and (match.result.name == team or team is None):
            if team is None:
                fouls = match.details[match.result.name].fouls
            else:
                fouls = match.details[team].fouls
            if fouls not in foul_wins:
                foul_wins[fouls] = 0
            foul_wins[fouls] += 1

    max_fouls = max(list(foul_wins.keys()))
    range_mappings = {}

    for i in range(0, max_fouls + 1, 4):
        range_str = str(i) + " - " + str(i + 3)
        range_mappings[i], range_mappings[i + 1], range_mappings[i + 2], range_mappings[i + 3] = (
            range_str,
            range_str,
            range_str,
            range_str,
        )

    foul_range_wins = {}
    for foul in foul_wins:
        range_mapping = range_mappings[foul]
        if range_mapping not in foul_range_wins:
            foul_range_wins[range_mapping] = 0
        foul_range_wins[range_mapping] += foul_wins[foul]

    optimal_fouls = [
        (
            foul_range,
            foul_range_wins[foul_range],
            str(round((foul_range_wins[foul_range] / len(matches)) * 100, 2)) + "%",
        )
        for foul_range in foul_range_wins
    ]
    sorted_optimal_fouls = sorted(optimal_fouls, key=lambda a: a[1], reverse=True)
    return sorted_optimal_fouls[:topx]


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["models.league"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
