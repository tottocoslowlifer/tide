import datetime as dt
import os
import re

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def call_moji_tide() -> pd.DataFrame:
    df_dir = "../../data/Moji_Tide_2011-2021/csv"
    if os.path.isdir(df_dir):
        df = pd.read_csv(df_dir +
                         "/9010_2011-2021.csv").drop("9010(門司の観測値コード)", axis=1)
        date_cols = ["20xx年", "xx月", "xx日"]

        df["年月日"] = [
            dt.date(
                2000 + int(df["20xx年"][i]),
                int(df["xx月"][i]),
                int(df["xx日"][i])
            )for i in range(len(df))
        ]
        df = df.drop(date_cols, axis=1)

        date_keys = []
        for i in range(len(df)):
            if df["年月日"][i] not in date_keys:
                date_keys.append(df["年月日"][i])

        am_cols = [f"{i}時の潮高値(cm)" for i in range(12)]
        pm_cols = [f"{i}時の潮高値(cm)" for i in range(12, 24)]

        new_df_list = []
        for i in range(len(date_keys)):
            tmp = df[df["年月日"] == date_keys[i]
                     ].reset_index().drop("index", axis=1)
            am_data = [item for item
                       in tmp[tmp["1(午前)/2(午後)"] == 1][am_cols].values[0]]
            pm_data = [item for item
                       in tmp[tmp["1(午前)/2(午後)"] == 2][am_cols].values[0]]
            new_df_list.append(am_data + pm_data)

        time_cols = am_cols + pm_cols
        df = pd.concat([pd.DataFrame(date_keys, columns=["年月日"]),
                        pd.DataFrame(new_df_list, columns=time_cols)], axis=1)

        date_dropped_df = df.drop("年月日", axis=1)
        index = list(date_dropped_df.dropna(how="all").index)

        return df.iloc[index].reset_index().drop("index", axis=1)
    else:
        print("Exceptional Error:")
        print(f"{df_dir} is not found")
        return 1


def get_label(df: pd.DataFrame, col: str) -> pd.DataFrame:
    labels_dict = {"小潮": 1, "中潮": 2, "大潮": 3, "若潮": 4, "長潮": 5}

    col_list = list(df[col])
    labels = [labels_dict[item] for item in col_list]
    df = df.drop(col, axis=1)
    df[col] = labels

    return df


def call_mooncal() -> pd.DataFrame:
    df_dir = "../../data/Moon_2011-2021"
    if os.path.isdir(df_dir):
        df = pd.read_csv(df_dir + "/Mooncal_2011-2021.csv")
        for item in ["こよみ", "気象庁", "MIRC"]:
            df = get_label(df, item)

        days = []

        time_format = "%Y-%m-%d"
        for i in range(len(df)):
            dtt = dt.datetime.strptime(df.loc[i, "年月日"], time_format)
            days.append(dt.date(dtt.year, dtt.month, dtt.day))

        longitude = []
        moonphase = []
        calendar = []
        jma = []
        mirc = []
        moon_dict = {"黄経差": longitude, "月齢": moonphase, "こよみ": calendar,
                     "気象庁": jma, "MIRC": mirc}
        for i in range(len(df)):
            for item in ["黄経差", "月齢", "こよみ", "気象庁", "MIRC"]:
                moon_dict[item].append(df.loc[i, item])

        return pd.DataFrame({"年月日": days, "黄経差": longitude, "月齢": moonphase,
                             "こよみ": calendar, "気象庁": jma, "MIRC": mirc})
    else:
        print("Exceptional Error:")
        print(f"{df_dir} is not found")
        return 1


def call_shimonoseki() -> pd.DataFrame:
    df_dir = "../../data/Shimonoseki_2011-2021"
    if os.path.isdir(df_dir):
        df = pd.read_csv(df_dir + "/Shimonoseki.csv").rename(
            columns={"Unnamed: 0": "年月日時"})

        times = []
        for i in range(len(df)):
            time = df.loc[i, "年月日時"]
            dt_ymd = dt.datetime.strptime(time.split("日")[0]+"日", "%Y年%m月%d日")
            dt_time = time.split("日")[1]

            if dt_time == "24時":
                dt_ymd = dt.date(dt_ymd.year, dt_ymd.month, dt_ymd.day)
                + dt.timedelta(days=1)
                dt_time = "0時"
            dt_time = dt.datetime.strptime(dt_time, "%H時")

            dt_ymd = dt.date(dt_ymd.year, dt_ymd.month, dt_ymd.day)
            dt_time = dt.time(dt_time.hour)
            times.append(dt.datetime.combine(dt_ymd, dt_time))
        rain = []
        temp = []
        item_dict = {"降水量(mm)": rain, "気温(℃)": temp}
        for i in range(len(df)):
            for item in ["降水量(mm)", "気温(℃)"]:
                if df.loc[i, item] == "--":
                    item_dict[item].append(float(0))
                elif df.loc[i, item] == "///":
                    item_dict[item].append(float("nan"))
                else:
                    df.loc[i, item] = "".join(
                        re.findall(r"\d+\.\d+", str(df.loc[i, item])))
                    if df.loc[i, item] == "":
                        df.loc[i, item] -= float("nan")
                    item_dict[item].append(float(df.loc[i, item]))

        return pd.DataFrame({"date": times, "rainfall(mm)": rain,
                             "temperature(℃)": temp})
    else:
        print("Exceptional Error:")
        print(f"{df_dir} is not found")
        return 1


def flatten(df: pd.DataFrame, how: str = "same") -> pd.DataFrame:
    time_cols = [f"{i}時の潮高値(cm)" for i in range(24)]
    label_cols = ["こよみ", "気象庁", "MIRC"]

    times = []
    data = []
    labels = []
    emd = []
    mp = []

    for i in range(len(df)):
        times += [dt.datetime.combine(df["年月日"][i], dt.time(time))
                  for time in range(24)]
        data += df[time_cols].iloc[i].to_list()

    for col in label_cols:
        tmp = []
        for i in range(len(df)):
            tmp += [df[col][i] for _ in range(24)]
        labels.append(tmp)

    if how == "diff":
        for i in range(len(df)):
            if i == len(df) - 1:
                emd_diff = (df["黄経差"][i] - df["黄経差"][i - 1]) / 24
                mp_diff = (df["月齢"][i] - df["月齢"][i - 1]) / 24

            else:
                emd_diff = (df["黄経差"][i + 1] - df["黄経差"][i]) / 24
                mp_diff = (df["月齢"][i + 1] - df["月齢"][i]) / 24

            emd += [df["黄経差"][i] + emd_diff * j for j in range(24)]
            mp += [df["月齢"][i] + mp_diff * j for j in range(24)]

    else:
        for i in range(len(df)):
            emd += [df["黄経差"][i] for _ in range(24)]
            mp += [df["月齢"][i] for _ in range(24)]

    return pd.DataFrame(
        {
            "date": times,
            "tide level": data,
            "longitude": emd,
            "moon phase": mp,
            "calendar": labels[0],
            "JMA": labels[1],
            "MIRC": labels[2],
        }
    )


def train_predict(X, y, split_rate):
    X_train, _, y_train, _ = train_test_split(
        X, y, test_size=split_rate, random_state=316
    )
    regressor = LinearRegression().fit(X_train, y_train)

    return regressor


def tide_shift(df: pd.DataFrame, num: int, drop: bool):
    pre_df = df.copy()
    X = []
    for i in range(num):
        X.append(f"tide level shift {i+1}h")
        pre_df[f"tide level shift {i+1}h"] = pre_df["tide level"].shift(i+1)

    if drop:
        pre_df = pre_df.dropna(subset=["rainfall(mm)", "temperature(℃)"])
        pre_df = pre_df.dropna(subset=["tide level"])
        pre_df = pre_df.dropna(subset=X)

    return pre_df, X


def main():
    new_dir = "../../data/Full_2011-2021"

    if os.path.isdir(new_dir):
        filenames = [new_dir + "/preprocessed_same.csv",
                     new_dir + "/preprocessed_diff.csv"]
        df = call_moji_tide()
        moon_df = call_mooncal()
        shimonoseki_df = call_shimonoseki()
        merged_df = pd.merge(df, moon_df, on="年月日", how="inner")
        for i in range(len(filenames)):
            if i == 0:
                flattened_df = flatten(merged_df, how="same")
            else:
                flattened_df = flatten(merged_df, how="diff")
            preprocessed_df = pd.merge(flattened_df, shimonoseki_df, on="date",
                                       how="inner").drop("date", axis=1)
            preprocessed_df_shift, new_cols = tide_shift(
                preprocessed_df, 10, True)
            cols = ["longitude", "moon phase", "calendar", "JMA", "MIRC",
                    "rainfall(mm)", "temperature(℃)"] + new_cols
            X = preprocessed_df_shift[cols]
            y = preprocessed_df_shift["tide level"]
            regressor = train_predict(X, y, 0.50)
            nan_tide_df = preprocessed_df[
                preprocessed_df["tide level"].isnull()]
            nan_tide_index = nan_tide_df.index

            for index in nan_tide_index:
                mra_df, _ = tide_shift(
                    preprocessed_df[index-10:1+index], 10, False)
                X_test = mra_df[cols].reset_index().drop("index",
                                                         axis=1).iloc[-1:]
                y_pred = round(regressor.predict(X_test)[0])
                preprocessed_df.loc[index, "tide level"] = y_pred
            preprocessed_df.to_csv(filenames[i])

    else:
        print("Exceptional Error:")
        print(f"{new_dir} is not found")


if __name__ == '__main__':
    main()
