import json

from experiment_tools.set_up import start_experiment
from utils.preprocessing import make_datasets


filename = "../../config/default/test.json"
with open(filename) as f:
    cfg = json.load(f)

logger = start_experiment(cfg)

df = make_datasets(cfg)
print(df)
