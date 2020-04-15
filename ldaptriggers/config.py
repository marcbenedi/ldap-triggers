import ruamel.yaml

from .params import CONFIG_PATH


class Config:
    def __init__(self):
        ldap_uri = 'ldap://vmniessner1.in.tum.de'        
        ldap_secret= '/etc/ldap.secret'
        self.load()

    def save(self):
        with open(CONFIG_PATH, 'w') as f:
            yaml.dump(self, f)

    def load(self):
        pass

yaml = ruamel.yaml.YAML()
yaml.register_class(Config)


config = Config()