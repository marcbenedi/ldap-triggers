import os
import sys
from pathlib import Path
import click
import ldap
import ruamel.yaml

from .params import *
from .config import config
from .model import Person, Group


yaml = ruamel.yaml.YAML()
yaml.register_class(Person)
yaml.register_class(Group)


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

def get_ldap_password():
    with open(config.ldap_secret, 'r') as file:
        password = file.read()
    return password.rstrip()

def fetch_ldap():
    """
    Fetched LDAP server information
    """
    con = ldap.initialize(config.ldap_uri)
    password = get_ldap_password()
    con.bind_s(config.admin, password, ldap.AUTH_SIMPLE)

    people = con.search_s(config.people, ldap.SCOPE_SUBTREE, '(objectclass=person)')
    people = list(map(lambda p: Person(p), people))
    groups = con.search_s(config.groups, ldap.SCOPE_SUBTREE, '(objectclass=posixGroup)')
    groups = list(map(lambda g: Group(g), groups))

    # Add extra groups to user
    for group in groups:
        for memberUid in group.memberUid:
            person = list(filter(lambda p: p.uid == memberUid, people))[0]
            person.groups.append(group.gidNumber)


    con.unbind_s()
    
    return people, groups

def store_to_yaml(object, path):
    print("Writing to %s"%path)
    with open(path, 'w') as f:
        yaml.dump(object, f)

def initialize():
    """
    Creates the required directories.
    """
    print("Creating directory /etc/ldaptriggers/")
    Path(PATH).mkdir(parents=True, exist_ok=True)
    # Create config file
    print("The following propmpts will configure /etc/ldaptriggers/config.yaml")
    config.ldap_uri = click.prompt('Enter ldap server uri', default='ldap://localhost')
    config.ldap_secret = click.prompt('Enter ldap server secret', default='/etc/ldap.secret')
    config.org = click.prompt('Enter ldap organization', default='dc=vc,dc=in,dc=tum,dc=de')  
    config.admin = click.prompt('Enter admin', default='cn=admin,') + config.org
    config.people = click.prompt('Enter people', default='ou=people,') + config.org
    config.groups = click.prompt('Enter groups', default='ou=groups,') + config.org
    config.save()
    # Create first ldap record
    sync = click.prompt('Do you want to sync with ldap now?', type=click.Choice(['Y', 'n']))
    if sync == 'Y':
        print("Synchronizing with ldap server...")
        people, groups = fetch_ldap()
        store_to_yaml(people, PEOPLE_PATH)
        store_to_yaml(groups, GROUPS_PATH)
    return None