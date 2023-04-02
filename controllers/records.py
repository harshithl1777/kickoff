"""Kickoff Project: controllers / records.py

This module contains functionality for finding various records in the datasets.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from typing import Optional
import heapq

from models.league import League
from models.team import Team
from utils.constants import Constants
from utils.league import get_all_matches

constant = Constants()


def most_goals_scored(league: League, season: Optional[str] = None, topx: int = 4) -> list[tuple[str, int]]:
    """Return a list of the topx teams that scored the most goals in the whole league

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
        - 0 < topx <= 20
    """
    matches = get_all_matches(league)
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


def most_improved_teams(league: League, season: str, top_x: int) -> list[tuple[str, int, int, int]]:
    """Return the top_x most improved teams in the given season in the league.
    The most improved team is calculated based on a computation on the team's winrate throughout the season.

    Each tuple in the returned list will be of the form
    (team name, worst winrate, final winrate, winrate improve)
    where
    team name is the name of the team,
    worst winrate is the lowest the team's winrate has been in the season*,
    final winrate is the winrate of the team at the end of the season,
    winrate improve is the difference between the final winrate and worst winrate

    The returned value is a list of length top_x, where each element is sorted
    in descending order by winrate improve.

    * worst winrate is calculated after ignoring the first 8 matches of the season.
    This is done because the teams winrate in the first few matches will be skewed.
    """
    team_improvements = []
    team_names = league.get_team_names(season)

    for team_name in team_names:
        team = league.get_team(team_name)
        improvement_statistic = _calculate_improvement_statistic(team, season)
        team_improvements.append(improvement_statistic)

    return heapq.nlargest(top_x, team_improvements, key=lambda x: x[3])


def most_clutch_team(league: League, season: Optional[str] = None, topx: int = 4) -> list[tuple[str, int, int]]:
    """Return a list of the most clutch teams in the specified season

    Preconditions:
        - season is in the format '20XX-XX' between 2009-10 and 2018-19
    """
    matches = get_all_matches(league)
    clutch = []
    max_clutch = 0

    print(len(matches))

    for match in matches:
        if season is None or match.season == season:
            if match.result is None:
                name = str(match.home_team.name) + " & " + str(match.away_team.name)
                if season is None:
                    name += f" ({match.season})"
                clutch.append((name, "0 - 0", "0 - 0", 0))
            else:
                name = match.result.name
                
                home_points_half = int(match.details[match.home_team.name].half_time_goals)
                away_points_half = int(match.details[match.away_team.name].half_time_goals)
                
                home_points_full = int(match.details[match.home_team.name].full_time_goals)
                away_points_full = int(match.details[match.away_team.name].full_time_goals)

                home_points_half_total = home_points_half - away_points_half
                away_points_half_total = away_points_half - home_points_half

                home_points_full_total = home_points_full - away_points_full
                away_points_full_total = away_points_full - home_points_full

                home_total = home_points_full_total - home_points_half_total
                away_total = away_points_full_total - away_points_half_total
            
            if season is None:
                name += f" ({match.season})"
            
            if max_clutch < home_total and max_clutch < away_total and home_total == away_total:
                max_clutch = home_total
                clutch.append((str(match.home_team.name) + " & " + str(match.away_team.name), int(home_points_half_total), int(home_points_full_total), int(home_total)))
            
            if max_clutch < home_total and home_total > away_total and home_points_half < away_points_half and home_points_full > away_points_full:
                max_clutch = home_total
                clutch.append((name, f"{abs(home_points_half)} - {abs(away_points_half)}", f"{abs(home_points_full)} - {abs(away_points_full)}", home_total))
            elif max_clutch < away_total and away_total > home_total and away_points_half < home_points_half and away_points_full > home_points_full:
                max_clutch = away_total
                clutch.append((name, f"{abs(home_points_half)} - {abs(away_points_half)}", f"{abs(home_points_full)} - {abs(away_points_full)}", away_total))
    
    return sorted(clutch, key=lambda clutch: clutch[3], reverse=True)[:topx]


def _calculate_improvement_statistic(team: Team, season: str) -> tuple():
    """Computed improvement statistic for the team in the specified season.

    Return a tuple of the form (team name, worst winrate, final winrate, winrate improve)

    The improvement statistic is calculated based on the computation described in most_improved_team.
    worst winrate, final winrate, and winrate improve are rounded to two decimal places

    Preconditions:
        - season in contants.retrieve("VALID_SEASONS")
    """
    winrate_progression = _calculate_winrate_progression(team, season)

    SKEW_IGNORE = 8  # number of intial matches to ignore due to skew
    final_winrate = winrate_progression[-1]
    worst_winrate = float("inf")
    for i in range(SKEW_IGNORE, len(winrate_progression) - 1):
        if winrate_progression[i] < worst_winrate:
            worst_winrate = winrate_progression[i]

    return (team.name,
            round(worst_winrate, 2),
            round(final_winrate, 2),
            round(final_winrate - worst_winrate, 2)
            )


def _calculate_winrate_progression(team: Team, season: str) -> list[float]:
    """Return a list of the team's winrate after each match in the specified season.

    The returned list will always be of length 38 - which is the total number of matches
    a team plays in a season of the Premier League.

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
        winrate = (matches_won / matches_played) * 100
        winrate_progression.append(winrate)

    return winrate_progression


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(
        config={
            "extra-imports": ["typing", "models.league"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
