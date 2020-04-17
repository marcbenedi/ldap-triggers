import unittest

from .context import ldaptriggers
from ldaptriggers.model import Person, Group

class PersonTestSuite(unittest.TestCase):
    """Person test cases."""

    def test_sample(self):
        self.assertEqual(1,2)

class GroupTestSuite(unittest.TestCase):
    """Person test cases."""

    def test_sample(self):
        self.assertEqual(1,2)