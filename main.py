"""Kickoff Project: main.py

This module creates the overall Typer application that is used to read commands / options 
from the user as a CLI. Primarily, it exports the app variable to all other files.

This file is Copyright (c) 2023 Ram Raghav Sharma, Harshith Latchupatula, Vikram Makkar and Muhammad Ibrahim.
"""

from cmd.commands import app
from utils.data import generate_pandas_df, convert_to_graph
from models.league import League

if __name__ == "__main__":
    # app()
    l = League()
    df = generate_pandas_df('./assets/season-0910.csv')
    convert_to_graph(df, l, "2009-10")
    print(l.matches[0])
    
