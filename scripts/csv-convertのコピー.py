import csv
import os


def time_editer(filename, writer):
    with open(filename) as f:
        file = f.readlines()
        for row in file:
            read = []
            read += [
                string(2000 + int(row[73:75])) + "/" + row[75:77] + "/" + row[77:79],
            ]
            for i in range(12):
                read.append(int(row[4 * i:4 * (i + 1)]))
        
            if row[79] == 2:
                read.append(row[69:73])

            writer.writerow(read)


def main():
    csv_dir = "../data/Moji_Tide_2011-2021/csv"

    raw_filename = csv_dir + "/9010_2011-2021_edited.csv"

    filename = csv_dir + "/9010_2011-2021_edited_time.csv"
    with open(filename, mode="w", newline="") as fw:
        writer = csv.writer(fw)

        writer.writerow(["ダウンロードした時刻：2024/2/11 19:37"])
        writer.writerow(
            [
                "xxxx年",
                "xx月",
                "xx日",
                "1(午前)/2(午後)",
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
                "9010(門司の観測値コード)"
            ]
        )

        for file in raw_filenames:
            time_editer(raw_filename, writer)


if __name__ == '__main__':
    main()
