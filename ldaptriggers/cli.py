import click
import time
from .utils import initialize, sudo, fetch_ldap, store_to_yaml
from .params import *
from .daemonize import daemonize
from .sync import sync
from . import signals


@click.command()
@click.option('-i', '--init', is_flag=True,
              help='Initializes configuration and directories. The default path is /etc/ldaptriggers.')
@click.option('-d', '--daemon', is_flag=True,
              help='Starts the program as a daemon.')
@click.option('-f', '--fetch', is_flag=True,
              help='Fetches ldap server and stores the info in people.yaml and groups.yaml but it does not execute any trigger.')
@click.option('-c', '--clear', is_flag=True,
              help='Clears all files from /etc/ldaptriggers/ and logs from /var/log/ldaptriggers.log. Calling it with --init will be required next time.')
def cli(init, daemon, fetch, clear):
    """
    LDAPTRIGGERS is a tool that allows triggering some actions when an LDAP change is detected.\n

    Entities supported: \n
        - Groups \n
        - Users \n
    Actions supported: \n
        - Add \n
        - Remove \n

    For example: If a User is modified, LDAPTRIGGERS would trigger Remove of that user and Add of the user (with the changes)    
    """
    sudo()
    if init:
        initialize()
    elif daemon:
        daemonize()
    elif fetch:
        people, groups = fetch_ldap()
        store_to_yaml(people, PEOPLE_PATH)
        store_to_yaml(groups, GROUPS_PATH)
    elif clear:
        pass
    else:
        # run in foreground
        while True:
            sync()
            time.sleep(TIMEOUT_DEBUG)
