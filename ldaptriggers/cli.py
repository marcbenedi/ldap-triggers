import click
from .utils import initialize, sudo


@click.command()
@click.option('--init', is_flag=True, help='Initializes configuration and directories. The default path is /etc/ldap-triggers')
@click.option('-d', '--deamon', is_flag=True, help='Deamonizes ldap-triggers')
@click.option('-s', '--sync', is_flag=True, help='Syncs with ldap server')
def cli(init, deamon, sync):
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
    if sync:
        pass
    
