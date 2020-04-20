from pathlib import Path

from .params import CONFIG_PATH
from .utils import read_from_yaml, store_to_yaml


class Config:
    def __init__(self):
        self.ldap_uri = 'ldap://localhost'
        self.ldap_secret = '/etc/ldap.secret'
        self.org = "dc=org,dc=company,dc=com"
        self.admin = "cn=admin," + self.org
        self.people = "ou=people," + self.org
        self.groups = "ou=groups," + self.org
        self.timeout = 60

        self.load()

    def save(self):
        store_to_yaml(self, CONFIG_PATH)

    def load(self):
        stored_config = Path(CONFIG_PATH)

        if stored_config.is_file():
            stored_config = read_from_yaml(CONFIG_PATH)

            self.ldap_uri = stored_config.ldap_uri
            self.ldap_secret = stored_config.ldap_secret
            self.org = stored_config.org
            self.admin = stored_config.admin
            self.people = stored_config.people
            self.groups = stored_config.groups
            self.timeout = stored_config.timeout


config = Config()
