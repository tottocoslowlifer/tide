import csv
import os


def csv_integrater(filename, writer):
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
    raw_dir = "../data/Shimonoseki_2011-2021"

    if os.path.isdir(raw_dir):
        raw_filenames = get_raw_data(raw_dir)

        csv_dir = raw_dir
        if os.path.isdir(csv_dir):
            pass
        else:
            os.mkdir(csv_dir)

        filename = csv_dir + "/Rain_2011-2021.csv"
        with open(filename, mode="w", newline="") as fw:
            writer = csv.writer(fw)

            writer.writerow(
                [
                    "20xx年xx月xx日xx時",
                    "降水量(mm)",
                    "均質番号"
                ]
            )

            for file in raw_filenames:
                raw_filename = raw_dir + "/" + file
                csv_integrater(raw_filename, writer)

    else:
        print("Exceptional Error:")
        print(f"{raw_dir} is not found")


if __name__ == '__main__':
    main()
