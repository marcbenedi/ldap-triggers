import click
from .utils import initialize, sudo, fetch_ldap, store_to_yaml
from .params import *

@click.command()
@click.option('--init', is_flag=True, help='Initializes configuration and directories. The default path is /etc/ldap-triggers')
@click.option('-d', '--deamon', is_flag=True, help='Deamonizes ldap-triggers')
@click.option('-f', '--fetch', is_flag=True, help='Fetch ldap server and stores the info')
def cli(init, deamon, fetch):
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
    if deamon:
        pass
    if fetch:
        people, groups = fetch_ldap()
        store_to_yaml(people, PEOPLE_PATH)
        store_to_yaml(groups, GROUPS_PATH)
