import logging
import logging.handlers
import os

from .params import LOG_PATH


_logger = None
"""
Holds the logger instance. It should not be accessed by the user.
To get the instance, get_logger() should be called instead.
"""

def _init_logger():
    """
    This function should not be called by the user.
    Configures the logger with the desired properties.
    This function should be only called by get_logger() if the current instance, _logger, has not yet been initialized.
    :return: Configured logger
    """
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
    """
    This function should be called to obtain the logger instance already configured.
    No new instance should be created by the user, only this function should be responsible of that.
    :return: Returns a logger
    """
    global _logger
    if _logger is None:
        _logger = _init_logger()
    return _logger
