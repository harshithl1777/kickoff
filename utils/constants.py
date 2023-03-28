"""Kickoff Project: utils / constants.py

This file contains the Constants class which holds various constants used throughout the application.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""
from typing import Any
from python_ta.contracts import check_contracts


# @check_contracts
class Constants:
    """This class contains a dictionary of constants that are used throughout this application."""

    _constants: dict[str, Any] = {}

    def __init__(self):
        self._constants["USE_COLUMNS"] = [
            "Date",
            "HomeTeam",
            "AwayTeam",
            "FTHG",
            "FTAG",
            "FTR",
            "HTHG",
            "HTAG",
            "HTR",
            "HS",
            "AS",
            "HST",
            "AST",
            "HF",
            "AF",
            "HY",
            "AY",
            "HR",
            "AR",
        ]
        self._constants["DATE_COLUMNS"] = ["Date"]
        self._constants[
            "HELP_COMMAND_INTRO"
        ] = "Kickoff is a football data analysis app that provides records and insights to football fans everywhere!"

    def retrieve(self, key: str) -> Any:
        """This function returns the corresponding constant when given the constant name.

        Preconditions:
            - key in self.constants
        """
        return self._constants[key]


if __name__ == "__main__":
    import python_ta

    python_ta.check_all()
