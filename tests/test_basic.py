import unittest

from .context import ldaptriggers

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_sample(self):
        self.assertEqual(1,1)