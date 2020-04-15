#!/home/marc/ldap-triggers/venv/bin/python 
import click

@click.command()
@click.option('--init', is_flag=True, help='Initialized configuration and directories. The default path is /etc/ldap-triggers')
@click.option('--deamon', is_flag=True, help='Deamonizes ldap-triggers')
def cli(init, deamon):
    pass

