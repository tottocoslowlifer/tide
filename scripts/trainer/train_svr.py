import json

from experiment_tools.set_up import start_experiment
from scripts.architectures.SVR import SVRModel
from utils.preprocessing import get_dataframe, make_datasets


filename = "../../config/default/SVR.json"
with open(filename) as f:
    cfg = json.load(f)

logger = start_experiment(cfg)

df = get_dataframe(cfg)
out = make_datasets(df, cfg)

model = SVRModel(cfg, X=out["X_train"], y=out["y_train"]["tide level"])
