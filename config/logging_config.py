import logging.config
import sys


def init_logging(config_path: str = "config/logging.ini"):
    logging.config.fileConfig(config_path, disable_existing_loggers=False)
