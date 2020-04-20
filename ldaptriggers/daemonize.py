"""
References: 
https://www.python.org/dev/peps/pep-3143/
https://pypi.org/project/python-daemon/
"""

import daemon
import time

from .sync import sync
from .config import config


def daemonize():
    """
    Runs the program as a daemon following PEP-3143.
    In summary, it means that the current session can be terminated and ldap-triggers will keep running in the backround.
    """
    with daemon.DaemonContext():
        while True:
            sync()
            time.sleep(config.timeout)
