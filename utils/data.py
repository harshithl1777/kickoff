"""Kickoff Project: utils / data.py

This file contains various functions that utilize the provided datasets and transform them into 
pandas DataFrames and League graphs.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

import pandas as pd
from python_ta.contracts import check_contracts

from utils.constants import USE_COLUMNS


@check_contracts
def generate_pandas_df(csv_file: str) -> None:
    """Initialize a DataTable class with the provided csv_file name and season.

    Preconditions:
        - csv_file is a valid csv file stored in the assets folder
    """
    dataframe = pd.read_csv(csv_file, usecols=USE_COLUMNS, parse_dates=["Date"])
    return dataframe


@check_contracts
def convert_to_graph(dataframe: pd.DataFrame) -> ...:
    """Muhammad, please write this docstring"""
    return NotImplementedError


if __name__ == "__main__":
    import python_ta

    python_ta.check_all()
