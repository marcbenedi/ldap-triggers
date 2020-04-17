# LDAP-triggers

## Dependencies

One of the requirements is python-ldap which is based on OpenLDAP, so you need to have the developemnt files (headers) in order to compile the Python module
```
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```

## Installation
```
pip install --editable .
```

## Important paths
Configuration /etc/ldaptriggers
Logs /var/log/ldaptriggers.log

## Run tests
```bash
make tests
```

## Trigger

/etc/ldaptriggers/triggers/

create scripts with [action]\_[entity]\_[name of script].bash
for example
add_people_slurm.bash

## License
This software is avaialble under the following licenses:
- MIT

For more details check LICENSE file

## Future work
- Lock pid file in order to allow only one instance
- Add cli entry to kill daeomon 
- Sig handling does not always work (at least with SIGTERM)
