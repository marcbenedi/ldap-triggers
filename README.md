# LDAP-triggers

## Dependencies

One of the requirements is python-ldap which is based on OpenLDAP, so you need to have the developemnt files (headers) in order to compile the Python module
```
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```

ldapsearch -x  -b ou=groups,dc=vc,dc=in,dc=tum,dc=de -h vmniessner1.in.tum.de

con.bind_s("cn=admin,dc=vc,dc=in,dc=tum,dc=de", "", ldap.AUTH_SIMPLE)
con.search_s("ou=groups,dc=vc,dc=in,dc=tum,dc=de", ldap.SCOPE_SUBTREE, '(objectclass=posixGroup)')
con.search_s("ou=people,dc=vc,dc=in,dc=tum,dc=de", ldap.SCOPE_SUBTREE, '(objectclass=person)')
con.unbind_s()

## Installation
```
pip install --editable .
```

## Important paths
Configuration /etc/ldaptriggers
Logs /var/log/ldaptriggers.log

## Future work
Lock pid file in order to allow only one instance
Add cli entry to kill daeomon 

## Trigger

/etc/ldaptriggers/triggers/

create scripts with [action]_[entity]_[name of script].bash
for example
add_people_slurm.bash