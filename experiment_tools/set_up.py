import logging
import platform
import subprocess

from experiment_tools.set_random_seed import fix_seed
from experiment_tools.start_logging import get_logger


def get_git_info(logger: logging.Logger) -> logging.Logger:
    git_info = "commit id: "
    git_info += subprocess.check_output(
        ["git", "rev-parse", "HEAD"]
    ).decode().strip()

    git_name = "username: "
    git_name += subprocess.check_output(
        ["git", "config", "user.name"]
    ).decode().strip()

    logger.info(git_info)
    logger.info(git_name)
    return logger


def get_os_info(logger: logging.Logger) -> logging.Logger:
    os_info = "\n\n"
    spec = [
        f"\tOS: {platform.system()} {platform.release()}",
        f"\tProcessor: {platform.processor()}",
        f"\tMachine: {platform.machine()}",
        f"\tNode: {platform.node()}",
        f"\tPython Version: {platform.python_version()}"
    ]
    for item in spec:
        os_info += item
        os_info += "\n"

    logger.info(f"OS infomation: {os_info}")
    return logger


def start_experiment(cfg: dict) -> logging.Logger:
    logger = get_logger(cfg)

    fix_seed(cfg["seed"])

    logger = get_git_info(logger)
    logger = get_os_info(logger)
