import logging
import logging.handlers
import os

from .params import LOG_PATH

_logger = None

def _init_logger():
    handler = logging.handlers.WatchedFileHandler(
        os.environ.get("LOGFILE", LOG_PATH)
    )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    logger.addHandler(handler)
    return logger

def get_logger():
    global _logger
    if _logger is None:
        _logger = _init_logger()
    return _logger