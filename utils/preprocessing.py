import pandas as pd
from sklearn.model_selection import train_test_split


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

    df["label"] = label_list

    return df


def make_datasets(df, cfg: dict) -> pd.DataFrame:
    path = cfg["data_path"]
    df = pd.read_csv(path, index_col=0)

    pre_df = df.copy().drop(
        [
            "longitude", "calendar", "JMA", "MIRC",
            "rainfall(mm)", "temperature(℃)",
        ],
        axis=1,
    )

    X_cols = []
    y_cols = ["tide level", "label"]
    for i in range(1, 13):
        title = f"tide level shift {i}h"
        X_cols.append(title)
        pre_df[title] = pre_df["tide level"].shift(i)
    X_cols.append("tide level shift 1y")
    pre_df["tide level shift 1y"] = pre_df["tide level"].shift(8570)
    X_cols.append("moon phase")

    X = pre_df[X_cols]
    y = pre_df[y_cols]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=cfg["split_rate"], random_state=316)

    out = {
        "datasets": pre_df,
        "X": X,
        "X_cols": X_cols,
        "y": y,
        "y_cols": y_cols,
        "X_train": X_train,
        "y_train": y_train,
        "X_test": X_test,
        "y_test": y_test,
    }

    return out
