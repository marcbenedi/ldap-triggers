# LDAP-triggers

![Tests](https://github.com/marcbenedi/ldap-triggers/workflows/Tests/badge.svg)

> This project is hosted at https://github.com/marcbenedi/ldap-triggers .

## Setup

```bash
$ ldaptriggers --init
# Follow instructions to set it up

$ ldaptriggers --daemon
# Or if you want to debug running it in foreground is recommended
$ ldaptriggers
```

## Dependencies

One of the requirements is python-ldap which is based on OpenLDAP, so you need to have the developemnt files (headers) in order to compile the Python module
```
sudo apt-get install gcc libpq-dev -y
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
sudo apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev
```

## Installation

At the moment this package is not available in *pip* repositories. To install it, create a virtual environment and install the requirements.

```
$ git clone https://github.com/marcbenedi/ldap-triggers
$ cd ldap-triggers
$ virtualenv -p python3 venv
$ pip install -r requirements.txt
$ pip install --editable .
```

## Important paths
Configuration files are stored in `/etc/ldaptriggers/`

The triggers are stored in `/etc/ldaptriggers/triggers`

Logs are stored in `/var/log/ldaptriggers.log`

## Run tests
```bash
make tests
```

## Triggers

Triggers are stored in `/etc/ldaptriggers/triggers/`

You can see some examples in this repository under `examples/triggers`

The name of the file is very important. It has to follow this pattern:

**[action]\_[entity]\_[name of script].bash**

For example, if we want a trigger to be executed when a user is added, it has to have the following name:

**add_people_send_email.bash**

If instead, we want a trigger when a group is deleted, it has to have the following name:

**delete_group_delete_shared_folder.bash**

> It is important that the triggers are executable by the root user, as the daemon is run by root

## License
This software is avaialble under the following licenses:
- MIT

For more details check LICENSE file

## Future work

Check the [project's board](https://github.com/marcbenedi/ldap-triggers/projects/) for more information and track current status. 

## Contributing

Check out [CONTRIBUTING.md](https://github.com/marcbenedi/ldap-triggers/blob/master/CONTRIBUTING.md) for more information.
