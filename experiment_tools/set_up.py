import logging
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
