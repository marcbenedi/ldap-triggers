import os
import sys
from pathlib import Path
import click

from .params import *
from .config import config

def sudo():
    """
    Check that the program is running as root, otherwise asks for permisions and runs again.
    """
    euid = os.geteuid()
    if euid != 0:
        print("Script not started as root. Running sudo...")
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        os.execlpe('sudo', *args) # Replaces the current process with the sudo

    print("Running as sudo")


def initialize():
    """
    Creates the required directories.
    """
    print("Creating directory /etc/ldaptriggers/")
    Path(PATH).mkdir(parents=True, exist_ok=True)
    # Create config file
    print("The following propmpts will configure /etc/ldaptriggers/config.yaml")
    ldap_uri = click.prompt('Enter ldap server uri', default='ldap://localhost')
    ldap_secret = click.prompt('Enter ldap server secret', default='/etc/ldap.secret')
    config.ldap_uri = ldap_uri
    config.ldap_secret = ldap_secret
    config.save()
    # Create first ldap record
    sync = click.prompt('Do you want to sync with ldap now?', type=click.Choice(['Y', 'n']))
    if sync == 'Y':
        print("Synchronizing with ldap server...")
    return None