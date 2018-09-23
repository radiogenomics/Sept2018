import os
import argparse
from argparse import ArgumentParser


def main(database: str, url_list_file: str ):
    print("we are going to work with " +database)
    print("we are going to scan " + url_list_file)

if __name__ == "__main__":
    bparser= argparse.ArgumentParser()
    bparser.add_argument("-db", "--database",help="SQLite File Name")
    bparser.add_argument("-i", "--input",help="SQLite File Name")
    bargs = bparser.parse_args()
    database_file = bargs.database
    input_file = bargs.input
    main(database=database_file, url_list_file=input_file)