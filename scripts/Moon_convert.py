import os

import pandas as pd


def get_raw_files(dir_path) -> list:
    filenames = []
    cnt = 2011

    for i in range(11):
        name = dir_path + "/raw/mooncal" + str(cnt+i) + ".csv"
        save_name = dir_path + "/raw/UTF-8_mooncal" + str(cnt+i) + ".csv"
        data = pd.read_csv(name, encoding="shift-jis")
        data.to_csv(save_name, index=False)
        filenames.append(save_name)
    return filenames


def main():
    raw_dir = "../data/Moon_2011-2021"
    csv_filename = raw_dir + "/Mooncal_2011-2021.csv"

    if os.path.isdir(raw_dir):
        raw_directories = get_raw_files(raw_dir)
        data = []
        for item in raw_directories:
            data.append(pd.read_csv(item))
        all_df = pd.concat(data).reset_index().drop("index", axis=1)
        all_df.to_csv(csv_filename, index=False)

    else:
        print("Exceptional Error:")
        print(f"{raw_dir} is not found")


if __name__ == '__main__':
    main()
