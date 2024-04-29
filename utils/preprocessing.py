import configparser
import os

import pandas as pd


def main():
    config_ini = configparser.ConfigParser()
    config_ini_path = "xxx.ini"  # 後ほど変更

    if not os.path.exists(config_ini_path):
        print("Exceptional Error:")
        print(f"{config_ini_path} is not found")

    config_ini.read(config_ini_path, encoding="utf-8")
    df = pd.read_csv(config_ini["D/S"])  # 後ほど変更
    return df


if __name__ == '__main__':
    main()
