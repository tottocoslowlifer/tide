import csv
import os


def csv_integrater(filename, writer):
    with open(filename, encoding="shift-jis") as f:
        file = f.readlines()[5:]
        for row in file:  
            row = row.rstrip()
            read = row.split(",")
            if read[1] == "--":
                read[1] = None
            writer.writerow(read)


def get_raw_dir(dir_path) -> list:
    dirnames = sorted(os.listdir(dir_path))
    dirnames.remove(".DS_Store")
    return dirnames


def get_raw_data(dir_path) -> list:
    filenames = sorted(os.listdir(dir_path))
    return filenames


def main():
    raw_dir = "../data/Shimonoseki_2011-2021"

    if os.path.isdir(raw_dir):
        raw_directories = get_raw_dir(raw_dir)
        for dcr in raw_directories:
            search_dir = raw_dir + "/" + dcr + "/raw"
            raw_filenames = get_raw_data(search_dir)

            filename = raw_dir + "/" + dcr + "/" + dcr + ".csv"
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
                    raw_filename = search_dir + "/" + file
                    csv_integrater(raw_filename, writer)    

    else:
        print("Exceptional Error:")
        print(f"{raw_dir} is not found")


if __name__ == '__main__':
    main()
