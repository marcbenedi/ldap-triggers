import signal
import sys

from .log import get_logger

def signal_handler(sig, frame):
    logger = get_logger()
    logger.warn('Signal received: ' + signal.Signals(sig).name)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)