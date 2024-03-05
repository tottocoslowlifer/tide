import pandas as pd


cnt = 2011
dir = "../data/Moon_2011-2021"
for i in range(10):
    data = pd.read_csv(dir + "/raw/mooncal" + str(cnt+i) + ".csv", encoding="shift-jis")
    data.to_csv(dir + "/" + str(cnt+i) + ".csv")