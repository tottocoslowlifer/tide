import pandas as pd


def get_dataframe(cfg: dict) -> pd.DataFrame:
    path = cfg["data_path"]
    df = pd.read_csv(path)
    return df
