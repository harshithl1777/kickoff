"""Kickoff Project: controllers / records.py

This module contains functionality for finding various records in the datasets.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from typing import Optional
import heapq

from models.league import League
from models.match import Match
from models.team import Team
from utils.constants import Constants


constant = Constants()


def most_goals_scored(league: League, season: Optional[str] = None, topx: int = 4) -> list[tuple[str, int]]:
    """Return a list of the topx teams that scored the most goals in the whole league

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - 0 < topx <= 20
    """
    matches = []
    season_orders = set()
    teams = league.get_team_names()
    for team in teams:
        team_matches = league.get_team(team).matches
        for match in team_matches:
            identifier = str(match.order) + match.season
            if identifier not in season_orders:
                matches.append(match)
                season_orders.add(identifier)
    goals = []

    for match in matches:
        if season is None or match.season == season:
            if match.result is None:
                winner_goals = match.details[match.home_team.name].full_time_goals
                team_name = str(match.home_team.name) + \
                    " & " + str(match.away_team.name)
            else:
                winner_goals = match.details[match.result.name].full_time_goals
                team_name = match.result.name

            if season is None:
                team_name += f" ({match.season})"

            goals.append((team_name, winner_goals))
    return sorted(goals, key=lambda goal: goal[1], reverse=True)[:topx]


def highest_win_streaks(league: League, season: str, topx: int = 4) -> list[tuple[str, int]]:
    """Return a list of the topx highest win streaks in the specified season

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - topx > 0
        - season is not None and topx <= 100
        - season is None and topx <= 20
    """
    team_names = league.get_team_names(season)
    streaks = []
    for name in team_names:
        team = league.get_team(name)
        matches = team.matches

        highest_streak = 0
        current_streak = 0
        for i in range(len(matches)):
            if matches[i].season == season:
                if matches[i].result == team:
                    current_streak += 1
                    if i == len(matches) - 1 and current_streak > highest_streak:
                        highest_streak = current_streak
                elif highest_streak < current_streak:
                    highest_streak = current_streak
                    current_streak = 0

        streaks.append((name, highest_streak))
    return sorted(streaks, key=lambda streak: streak[1], reverse=True)[:topx]


def _calculate_improvement_statistic(team: Team, season: str) -> tuple():
    """Computed improvement statistic for the team in the specified season.

    Return a tuple of the form (team name, worst winrate, final winrate, winrate improve)

    The improvement statistic is calculated based on the computation described in most_improved_team

    Preconditions:
        - season in contants.retrieve("VALID_SEASONS")
    """
    winrate_progression = _calculate_winrate_progression(team, season)

    SKEW_IGNORE = 8  # number of intial matches to ignore due to skew
    final_winrate = winrate_progression[-1]
    worst_winrate = float("-inf")
    for i in range(SKEW_IGNORE + 1, len(winrate_progression) - 1):
        if winrate_progression[i] < worst_winrate:
            worst_winrate = winrate_progression[i]

    return team.name, worst_winrate, final_winrate, final_winrate - worst_winrate


def _calculate_winrate_progression(team: Team, season: str) -> list[float]:
    """Return a list of the team's winrate after each match in the specified season.

    The returned list will always be of length 38 - which is the number of matches
    a team plays in a season of the Premier League

    Preconditions:
        - season in contants.retrieve("VALID_SEASONS")
    """
    matches_won = 0
    matches_played = 0
    winrate_progression = []

    for match in team.matches:
        if match.season != season:
            continue
        matches_played += 1
        if match.result == team:
            matches_won += 1
        winrate = (matches_won / matches_won) * 100
        winrate_progression.append(winrate)

    return winrate_progression
