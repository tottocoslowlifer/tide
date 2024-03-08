import os

import pandas as pd


def get_raw_dir(dir_path) -> list:
    dirnames = sorted(os.listdir(dir_path))
    if ".DS_Store" in dirnames:
        dirnames.remove(".DS_Store")
    return dirnames


def main():
    raw_dir = "../data/Shimonoseki_2011-2021"

    if os.path.isdir(raw_dir):
        raw_directories = get_raw_dir(raw_dir)
        dcr_dict = {"Rain_2011-2021": "降水量(mm)", "Temp_2011-2021": "気温(℃)"}
        df_list = []

        for dcr in raw_directories:
            search_dir = raw_dir + "/" + dcr + "/raw"
            raw_filenames = get_raw_dir(search_dir)
            filename = raw_dir + "/" + dcr + "/" + dcr + ".csv"

            data = []
            for item in raw_filenames:
                data.append(pd.read_csv(
                    search_dir+"/"+item, encoding="shift_jis", header=3,
                    index_col=0, names=[dcr_dict[dcr], "均質番号"]
                ))
            all_df = pd.concat(data).drop("均質番号", axis=1)
            df_list.append(all_df)
            all_df.to_csv(filename)

        concat_df = pd.concat(df_list, axis=1)
        concat_df.to_csv(raw_dir + "/Shimonoseki.csv")

    else:
        print("Exceptional Error:")
        print(f"{raw_dir} is not found")


if __name__ == '__main__':
    main()
