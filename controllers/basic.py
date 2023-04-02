"""Kickoff Project: controllers / basic.py

This module contains functionality for performing basic analysis on the premier league data.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""
from typing import Optional

from models.league import League
from utils.league import get_all_matches


def overall_winrate(league: League, team_name: str, season: Optional[str] = None) -> float:
    """Return the overall winrate (as a percentage) of the Team with team_name in the League.
    Only consider matches in the season if the season is provided.

    Preconditons:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in league._teams
        - If the season is provided, the team took part in that season
    """
    total_matches = 0
    total_wins = 0

    team = league.get_team(team_name)
    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        if match.result == team:
            total_wins += 1

    return (total_wins / total_matches) * 100

def home_vs_away(league: League, team_name: Optional[str] = None, season: Optional[str] = None) -> list[tuple[float, float, float]]:
    """Return the home winrate (as a percentage) and away wintrate (as a percentage) of the Team with team_name in the League.
    Only consider matches in the season if the season is provided.

    Preconditons:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in league._teams
        - If the season is provided, the team took part in that season
    """
    home_win_rate = 0
    away_win_rate = 0
    draws = 0
    
    if team_name is not None:
        team = league.get_team(team_name)
        for match in team.matches:
            if season is not None and match.season != season:
                continue
            if match.home_team == team:
                if match.result == team:
                    home_win_rate += 1
            elif match.away_team == team:
                if match.result == team:
                    away_win_rate += 1
            else:
                draws += 1
        home_win_rate = (home_win_rate / len(team.matches)) * 100
        away_win_rate = (away_win_rate / len(team.matches)) * 100
        draws = (draws / len(team.matches)) * 100
    else:
        matches = get_all_matches(league)
        for match in matches:
            if season is not None and match.season != season:
                continue
            if match.home_team == match.result:
                home_win_rate += 1
            elif match.away_team == match.result:
                away_win_rate += 1
            else:
                draws += 1
        home_win_rate = (home_win_rate / len(matches)) * 100
        away_win_rate = (away_win_rate / len(matches)) * 100
        draws = (draws / len(matches)) * 100
    
    return [(round(home_win_rate, 2), round(away_win_rate, 2), round(draws, 2))]
    


def get_team_goals_scored(league: League, team_name: str, season: Optional[str] = None) -> float:
    """Return the average number of goals scored by a team in their matches.
    Consider the matches in a specific season if it is provided.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in league._teams
        - If the season is provided, the team took part in that season
    """
    total_matches = 0
    goals_scored = 0
    team = league.get_team(team_name)

    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        goals_scored += match.details[team_name].full_time_goals

    return goals_scored / total_matches


def get_team_shot_accuracy(league: League, team_name: str, season: Optional[str] = None) -> float:
    """Return the average shot accuracy (as a percentage) of a given team in their matches.
    Consider the matches in a specific season if it is provided.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in league._teams
        - If the season is provided, the team took part in that season
    """
    total_matches = 0
    accuracy = 0
    team = league.get_team(team_name)

    for match in team.matches:
        if season is not None and match.season != season:
            continue
        shots = match.details[team_name].shots
        if shots==0:
            continue
        total_matches += 1
        shots_target = match.details[team_name].shots_on_target     
        accuracy += (shots_target/shots)
        
    return (accuracy / total_matches) * 100


def get_team_fouls(league: League, team_name: str, season: Optional[str] = None) -> float:
    """Return the average number of fouls committed by a team in their matches.
    Consider the matches in a specific season if it is provided.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in league._teams
        - If the season is provided, the team took part in that season
    """
    total_matches = 0
    fouls = 0
    team = league.get_team(team_name)

    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        fouls += match.details[team_name].fouls

    return fouls / total_matches


def get_team_cards(league: League, team_name: str, season: Optional[str] = None) -> float:
    """Return the average number of card offenses received by a team in their matches.
    Yellow cards will be counted as one point and red cards will be counted as two points.
    Consider the matches in a specific season if it is provided.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
        - team_name in self._teams
        - If the season is provided, the team took part in that season
    """
    total_matches = 0
    cards = 0
    team = league.get_team(team_name)

    for match in team.matches:
        if season is not None and match.season != season:
            continue
        total_matches += 1
        cards += match.details[team_name].yellow_cards
        cards += 2 * (match.details[team_name].red_cards)

    return cards / total_matches


def get_season_goals_scored(league: League, season: str) -> float:
    """Return the average number of goals scored in a match by all teams in a season.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
    """
    team_names = league.get_team_names(season)
    team_goals_scored = []

    for name in team_names:
        team_goals_scored.append(get_team_goals_scored(league, name, season))

    return (sum(team_goals_scored)) / len(team_goals_scored)


def get_season_shot_accuracy(league: League, season: str) -> float:
    """Return the average shot accuracy in a match by all teams in a season.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
    """
    team_names = league.get_team_names(season)
    team_accuracy = []

    for name in team_names:
        team_accuracy.append(get_team_shot_accuracy(league, name, season))

    return (sum(team_accuracy)) / len(team_accuracy)


def get_season_fouls(league: League, season: str) -> float:
    """Return the average fouls committed in a match by all teams in a season.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
    """
    team_names = league.get_team_names(season)
    team_fouls = []

    for name in team_names:
        team_fouls.append(get_team_fouls(league, name, season))

    return (sum(team_fouls)) / len(team_fouls)


def get_season_cards(league: League, season: str) -> float:
    """Return the average card offenses received in a match by all teams in a season.

    Preconditions:
        - season in ['2009-10', '2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17', \
        '2017-18', '2018-19']
    """
    team_names = league.get_team_names(season)
    team_cards = []

    for name in team_names:
        team_cards.append(get_team_cards(league, name, season))

    return (sum(team_cards)) / len(team_cards)



if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["typing", "models.league"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
