import csv
import os
import pandas as pd


def to_column(r_filename, e_filename, column):
    df = pd.read_csv(r_filename)

    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month

    df_agg = df.groupby(column).agg(["mean", "max", "min"])
    df_agg.to_csv(e_filename)


def main():
    raw_dir = "../data/Moji_Tide_2011-2021/csv"

    edit_dir = raw_dir

    raw_filename = raw_dir + "/9010_2011-2021_edited.csv"

    columns = ["Date","Year","Month"]
    for column in columns:
        edit_filename = edit_dir + "/9010_2011-2021_edited_{}.csv", column
        to_column(raw_filename, edit_filename, column)


if __name__ == '__main__':
    main()
