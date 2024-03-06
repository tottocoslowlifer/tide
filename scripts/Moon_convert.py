import csv
import os

import pandas as pd


def csv_integrater(filename, writer):
    with open(filename) as f:
        file = f.readlines()[1:]
        for row in file:
            row = row.rstrip()
            read = row.split(",")
            writer.writerow(read)


def get_raw_files(dir_path) -> list:
    filenames = []
    cnt = 2011

    for i in range(11):
        name = dir_path + "/raw/mooncal" + str(cnt+i) + ".csv"
        data = pd.read_csv(name, encoding="shift-jis", index_col=0)
        data.to_csv(name, index=False)
        filenames.append(name)
    return filenames


def main():
    raw_dir = "../data/Moon_2011-2021"

    csv_filename = raw_dir + "/Mooncal_2011-2021.csv"

    if os.path.isdir(raw_dir):
        raw_directories = get_raw_files(raw_dir)
        with open(csv_filename, mode="w", newline="") as fw:
            writer = csv.writer(fw)
            writer.writerow(
                [
                    "月日",
                    "黄経差",
                    "月齢",
                    "こよみ",
                    "気象庁",
                    "MIRC"
                ]
            )
            for file in raw_directories:
                csv_integrater(file, writer)

    else:
        print("Exceptional Error:")
        print(f"{raw_dir} is not found")


if __name__ == '__main__':
    main()
