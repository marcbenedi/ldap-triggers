"""
References: 
https://www.python.org/dev/peps/pep-3143/

https://pypi.org/project/python-daemon/
"""

import daemon
import time

from .sync import sync

def daemonize():
    with daemon.DaemonContext():
        while(True):
            sync()
            time.sleep(60)