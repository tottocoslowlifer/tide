import logging
import platform
import subprocess


def get_git_info(logger) -> logging.Logger:
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
