import ruamel.yaml
from pathlib import Path

from .params import CONFIG_PATH


class Config:
    def __init__(self):
        self.ldap_uri = 'ldap://localhost'
        self.ldap_secret = '/etc/ldap.secret'
        self.org = "dc=org,dc=company,dc=com"
        self.admin = "cn=admin," + self.org
        self.people = "ou=people," + self.org
        self.groups = "ou=groups," + self.org

        self.load()

    def save(self):
        with open(CONFIG_PATH, 'w') as f:
            yaml.dump(self, f)

    def load(self):
        stored_config = Path(CONFIG_PATH)
        if stored_config.is_file():
            with open(CONFIG_PATH, 'r') as f:
                stored_config = yaml.load(f)
                self.ldap_uri = stored_config.ldap_uri
                self.ldap_secret = stored_config.ldap_secret
                self.org = stored_config.org
                self.admin = stored_config.admin
                self.people = stored_config.people
                self.groups = stored_config.groups


yaml = ruamel.yaml.YAML()
yaml.register_class(Config)

config = Config()
