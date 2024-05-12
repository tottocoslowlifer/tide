import pandas as pd


def get_dataframe(cfg: dict) -> pd.DataFrame:
    path = cfg["data_path"]
    df = pd.read_csv(path, index_col=0)

    label_list = []
    for i in range(len(df)):
        tide = df.loc[i, "tide level"]
        if tide > 200.00:
            label_list.append(1)  # 門司港レトロクルーズ
        elif tide > 150.00:
            label_list.append(2)  # 関門海峡クルージング
        elif tide > 100.00:
            label_list.append(3)  # 巌流島上陸
        else:
            label_list.append(4)   # 運行中止

    label_df = pd.DataFrame(label_list, columns=["label"])
    df = pd.concat([label_df, df], axis=1)

    return df


def make_datasets(cfg: dict) -> pd.DataFrame:
    path = cfg["data_path"]
    df = pd.read_csv(path, index_col=0)

    pre_df = df.copy().drop(["longitude", "calendar", "JMA", "MIRC",
                             "rainfall(mm)", "temperature(℃)"], axis=1)
    X = []
    for i in range(1, 13):
        X.append(f"tide level shift {i}h")
        pre_df[f"tide level shift {i}h"] = pre_df["tide level"].shift(i)

    X.append("tide level shift 1y")
    pre_df["tide level shift 1y"] = pre_df["tide level"].shift(8570)

    return pre_df
