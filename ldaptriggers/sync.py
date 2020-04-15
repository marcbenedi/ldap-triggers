#!/home/marc/ldap-triggers/venv/bin/python 
import sys
sys.path.append('.')

import ldap
from params import LDAP_URI
from params import LDAP_SECRET
from params import PATH, GROUPS_PATH, PEOPLE_PATH
from model import Person, Group
import ruamel.yaml

ORG = "dc=vc,dc=in,dc=tum,dc=de"
ADMIN = "cn=admin," + ORG
PEOPLE = "ou=people," + ORG
GROUPS = "ou=groups," + ORG

def get_ldap_password():
    with open(LDAP_SECRET, 'r') as file:
        password = file.read()
    return password.rstrip()

# TODO: Implement more efficiently
def diff_left(l1, l2):
    diff = l1.copy()
    for e2 in l2:
        for e1 in l1: 
            if e1 == e2:
                diff.remove(e1)

    return diff

yaml = ruamel.yaml.YAML()
yaml.register_class(Person)
yaml.register_class(Group)

old_people = []
old_groups = []

with open(PEOPLE_PATH, 'r') as f:
    old_people = yaml.load(f)
with open(GROUPS_PATH, 'r') as f:
    old_groups = yaml.load(f)

con = ldap.initialize(LDAP_URI)

password = get_ldap_password()
con.bind_s(ADMIN, password, ldap.AUTH_SIMPLE)

people = con.search_s(PEOPLE, ldap.SCOPE_SUBTREE, '(objectclass=person)')
people = list(map(lambda p: Person(p), people))
groups = con.search_s(GROUPS, ldap.SCOPE_SUBTREE, '(objectclass=posixGroup)')
groups = list(map(lambda g: Group(g), groups))

# Add extra groups to user
for group in groups:
    for memberUid in group.memberUid:
        person = list(filter(lambda p: p.uid == memberUid, people))[0]
        person.groups.append(group.gidNumber)


con.unbind_s()

print(old_people == people)
print(old_groups == groups)

deleted_people = diff_left(old_people, people) 
added_people = diff_left(people, old_people)
deleted_groups = diff_left(old_groups, groups) 
added_groups = diff_left(groups, old_groups)


with open(PEOPLE_PATH, 'w') as f:
    yaml.dump(people, f)
with open(GROUPS_PATH, 'w') as f:
    yaml.dump(groups, f)