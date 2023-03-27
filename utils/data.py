import pandas as pd
from python_ta.contracts import check_contracts

from constants import USE_COLUMNS


@check_contracts
class DataTable:
    def __init__(self, csv_file: str, season: tuple[int, int]) -> pd.DataFrame:
        """Initialize a DataTable class with the provided csv_file name and season."""
        dataframe = pd.read_csv(csv_file, usecols=USE_COLUMNS, parse_dates=["Date"])
        return dataframe

    def convert_to_graph(self) -> ...:
        return NotImplementedError


if __name__ == "__main__":
    import python_ta

    python_ta.check_all()
