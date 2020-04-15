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