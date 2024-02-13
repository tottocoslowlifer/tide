import csv
import os


def txt_csv_converter(filename, writer):
    with open(filename) as f:
        file = f.readlines()
        for row in file:
            read = []
            for i in range(12):
                if int(row[4 * i:4 * (i + 1)]) == 9999:
                    read.append(None)
                else:
                    read.append(int(row[4 * i:4 * (i + 1)])) 
            read += [
                int(row[69:73]),
                int(row[73:75]),
                int(row[75:77]),
                int(row[77:79]),
                int(row[79]),
            ]
            writer.writerow(read)


def get_raw_data(dir_path) -> list: 
    filenames = sorted(os.listdir(dir_path)) 
    return filenames 


def main():
    raw_dir = "data/Moji_Tide_2011-2021/raw"

    if os.path.isdir(raw_dir): 
        raw_filenames = get_raw_data(raw_dir)

        csv_dir = "data/Moji_Tide_2011-2021/csv"
        if os.path.isdir(csv_dir): 
            pass
        else: 
            os.mkdir(csv_dir)

        filename = csv_dir + "/9010_2011-2021.csv"
        with open(filename, mode="w", newline="") as fw:
            writer = csv.writer(fw)

            writer.writerow(["ダウンロードした時刻：2024/2/11 19:37"])
            writer.writerow(
                [
                    "0時の潮高値(cm)",
                    "1時の潮高値(cm)",
                    "2時の潮高値(cm)",
                    "3時の潮高値(cm)",
                    "4時の潮高値(cm)",
                    "5時の潮高値(cm)",
                    "6時の潮高値(cm)",
                    "7時の潮高値(cm)",
                    "8時の潮高値(cm)",
                    "9時の潮高値(cm)",
                    "10時の潮高値(cm)",
                    "11時の潮高値(cm)",
                    "9010(門司の観測値コード)",
                    "20xx年",
                    "xx月",
                    "xx日",
                    "1(午前)/2(午後)",
                ]
            )

            for file in raw_filenames:
                raw_filename = raw_dir + "/" + file
                txt_csv_converter(raw_filename, writer)

    else: 
        print("Exceptional Error:")
        print(f"{raw_dir} is not found")


if __name__ == '__main__':
    main()
