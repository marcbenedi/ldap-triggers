import unittest

from .context import ldaptriggers
from ldaptriggers.model import Person, Group

class PersonTestSuite(unittest.TestCase):
    """Person test cases."""

    def setUp(self):
        self.people = [
            (
                'cn=John Smith,ou=people,dc=myorg,dc=company,dc=com', 
                {
                    'givenName': ['John'],
                    'shadowMin': ['1'],
                    'shadowWarning': ['10'],
                    'uid': ['smith'],
                    'homeDirectory': ['/home/smith'],
                    'uidNumber': ['10000'],
                    'shadowInactive': ['10'],
                    'sn': ['Smith'],
                    'cn': ['John Smith'],
                    'gidNumber': ['10000'],
                    'objectClass': ['shadowAccount', 'posixAccount', 'inetOrgPerson', 'organizationalPerson', 'person'],
                    'shadowMax': ['365'],
                    'loginShell': ['/bin/bash']
                }
            )
        ]

    def tearDown(self):
        self.tuple = None

    def test_sample(self):
        self.assertEqual(1,1)

    def test_init_success(self):
        tuple = self.people[0]
        person = Person(tuple)

class GroupTestSuite(unittest.TestCase):
    """Person test cases."""

    def setUp(self):
        self.groups = [
            (
                'cn=software,ou=groups,dc=myorg,dc=company,dc=com', 
                {
                    'cn': ['software'],
                    'gidNumber': ['10000'],
                    'objectClass': ['posixGroup']
                }
            ), 
            (
                'cn=hardware,ou=groups,dc=myorg,dc=company,dc=com', 
                {
                    'cn': ['hardware'],
                    'gidNumber': ['10001'],
                    'objectClass': ['posixGroup']
                }
            )
        ]

    def tearDown(self):
        self.groups = None

    def test_sample(self):
        self.assertEqual(1,1)
        
    # test __init__

    # test __eq__