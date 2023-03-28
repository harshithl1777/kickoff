"""Kickoff Project: utils / data.py

This file contains various functions that utilize the provided datasets and transform them into 
pandas DataFrames and League graphs.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

import pandas as pd
from python_ta.contracts import check_contracts

from utils.constants import Constants
from models.league import League
from models.match import Match, MatchDetails
from models.team import Team


@check_contracts
def generate_pandas_df(csv_file: str) -> pd.DataFrame:
    """Initialize a DataTable class with the provided csv_file name and season.

    Preconditions:
        - csv_file is a valid csv file stored in the assets folder
    """
    constants = Constants()
    dataframe = pd.read_csv(
        csv_file, usecols=constants.retrieve("USE_COLUMNS"), parse_dates=constants.retrieve("DATE_COLUMNS")
    )
    return dataframe


@check_contracts
def convert_to_graph(dataframe: pd.DataFrame, league: League) -> None:
    """Populate the graph with the provided dataframe representing the match and overall season statistics

    Preconditions:
        - dataframe is a valid representation of a csv file stored in the assets folder
    """

    # TODO: Not sure how to work with pandas dataframe, someone take a look and edit as necessary
    for row in dataframe:  
        if row[home_team] not in league.teams:
            home_team = Team(row["HomeTeam"], [])
        else:
            home_team = league.teams[row["HomeTeam"]]

        if row[away_team] not in league.teams:
            away_team = Team(row["AwayTeam"], [])
        else:
            away_team = league.teams[row["AwayTeam"]]
        

        home_team_details = MatchDetails(home_team, row["HF"], row["HS"], row["HST"], row["HR"], row["HY"], row["HTHG"], row["FTHG"])
        away_team_details = MatchDetails(away_team, row["AF"], row["AS"], row["AST"], row["AR"], row["AY"], row["HTAG"], row["FTAG"])
        result_status = {"H": "HOME_WIN", "A": "AWAY_WIN", "D": "DRAW"}

        # TODO: Fix date and season attribute
        match = Match('season', home_team, away_team, 'date', {home_team: home_team_details, away_team: away_team_details}, result_status[row["FTR"]])
        home_team.matches.append(match)
        away_team.mathes.append(match)

if __name__ == "__main__":
    import python_ta

    python_ta.check_all()
