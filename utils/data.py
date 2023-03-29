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


# @check_contracts
def generate_pandas_dataframe(csv_file: str) -> pd.DataFrame:
    """Initialize a DataTable class with the provided csv_file name and season.

    Preconditions:
        - csv_file is a valid csv file stored in the assets folder
    """
    constants = Constants()
    dataframe = pd.read_csv(
        csv_file, usecols=constants.retrieve("USE_COLUMNS"), parse_dates=constants.retrieve("DATE_COLUMNS")
    )
    dataframe.sort_values(by="Date", inplace=True)
    return dataframe


# @check_contracts
def convert_to_graph(dataframe: pd.DataFrame, league: League, season: str) -> League:
    """Populate the graph with the provided dataframe representing the match and overall season statistics

    Preconditions:
        - dataframe is a valid representation of a csv file stored in the assets folder
        - season is a season string in the format '20XX-XX'
    """
    for i in range(len(dataframe.index)):
        ht_name = dataframe["HomeTeam"][i]
        at_name = dataframe["AwayTeam"][i]

        if not league.team_in_league(ht_name):
            home_team = league.add_team(ht_name)
        else:
            home_team = league.get_team(ht_name)

        if not league.team_in_league(at_name):
            away_team = league.add_team(at_name)
        else:
            away_team = league.get_team(at_name)

        home_team_details = MatchDetails(
            team=home_team,
            fouls=dataframe["HF"][i],
            shots=dataframe["HS"][i],
            shots_on_target=dataframe["HST"][i],
            red_cards=dataframe["HR"][i],
            yellow_cards=dataframe["HY"][i],
            half_time_goals=dataframe["HTHG"][i],
            full_time_goals=dataframe["FTHG"][i],
        )
        away_team_details = MatchDetails(
            team=away_team,
            fouls=dataframe["AF"][i],
            shots=dataframe["AS"][i],
            shots_on_target=dataframe["AST"][i],
            red_cards=dataframe["AR"][i],
            yellow_cards=dataframe["AY"][i],
            half_time_goals=dataframe["HTAG"][i],
            full_time_goals=dataframe["FTAG"][i],
        )

        if dataframe["FTR"][i] == "H":
            result = home_team
        elif dataframe["FTR"][i] == "A":
            result = away_team
        else:
            result = None

        details = {ht_name: home_team_details, at_name: away_team_details}
        match = Match(
            season=season, home_team=home_team, away_team=away_team, order=(i + 1), details=details, result=result
        )

        league.add_match(ht_name, at_name, match)

        return league


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            "extra-imports": ["__future__", "dataclasses", "match"],
            "allowed-io": [],
            "max-line-length": 120,
        }
    )
