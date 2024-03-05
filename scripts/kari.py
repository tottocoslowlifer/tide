import csv
import os


def csv_integrater(filename, writer):
    with open(filename, encoding="shift-jis") as f:
        file = f.readlines()
        for row in file:  
            row = row.rstrip()
            read = row.split(",")
            #if read[1] == "--":
                #read[1] = None
            writer.writerow(read)


def get_raw_dir(dir_path) -> list:
    dirnames = sorted(os.listdir(dir_path))
    return dirnames


def get_raw_data(dir_path) -> list:
    filenames = sorted(os.listdir(dir_path))
    return filenames


def main():
    raw_dir = "../data/Shimonoseki_2011-2021"

    if os.path.isdir(raw_dir):
        raw_directories = get_raw_dir(raw_dir)
        for dcr in raw_directories:
            search_dir = raw_dir + "/" + dcr
            #raw_filenames = get_raw_data(search_dir)
            print(search_dir)
    else:
        print("Exceptional Error:")
        print(f"{raw_dir} is not found")


if __name__ == '__main__':
    main()
