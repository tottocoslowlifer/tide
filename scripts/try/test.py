import json

from experiment_tools.set_up import start_experiment


filename = "../../config/default/test.json"
with open(filename) as f:
    cfg = json.load(f)

logger = start_experiment(cfg)