import os
import logging.config


def init_logging(config_path: str = "config/logging.ini"):
    # Ensure logs directory exists
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    logging.config.fileConfig(config_path, disable_existing_loggers=False)
