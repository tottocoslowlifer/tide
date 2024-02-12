import csv
import pathlib

def txt_csv_converter(datas,f,writers):
    with open(datas)as rf:
        readfile = rf.readlines()
        for read_text in readfile:
            read = []
            for i in range(12):
                read += [read_text[4*i:4*i+4]]
            read += [read_text[69:73],read_text[73:75],read_text[75:77],read_text[77:79],read_text[79]]
            writer.writerow(read)

new_file = pathlib.Path("9010_2011-2021.csv")
wf = open(new_file, mode="w", newline="")
writer = csv.writer(wf,delimiter = ",")
writer.writerow(["ダウンロードした時刻：2024/2/11 19:37"])
writer.writerow(["0時の潮高値(cm)","1時の潮高値(cm)","2時の潮高値(cm)","3時の潮高値(cm)","4時の潮高値(cm)","5時の潮高値(cm)","6時の潮高値(cm)","7時の潮高値(cm)","8時の潮高値(cm)","9時の潮高値(cm)","10時の潮高値(cm)","11時の潮高値(cm)","9010(門司の観測値コード)","20xx年","xx月","xx日","1(午前)/2(午後)"])

years = 11
for i in range(years):
    file_name = f"9010_{2011+i}.txt"
    txt_csv_converter(file_name,wf,writer)
wf.close()
