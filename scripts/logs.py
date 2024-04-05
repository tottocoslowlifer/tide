import json
import logging
from logging import getLogger, FileHandler, Formatter
import subprocess


def set_logging(cfg):
    logger = getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = FileHandler(cfg["log"]["log_file"], mode='w')
    formatter = Formatter(cfg["log"]["log_formatter"])
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


filename = "../config/default/test.json"
with open(filename) as f:
    cfg = json.load(f)

logger = set_logging(cfg)

git_info = "commit id: "
git_info += subprocess.check_output(
    ['git', 'rev-parse', 'HEAD']
).decode().strip()
logger.info(git_info)
logger.info(f"username: {cfg['name']}")
logger.info(cfg["greeting"] * cfg["reps"])
