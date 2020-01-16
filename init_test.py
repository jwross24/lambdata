import unittest
from lambdata_jwross24 import increment


class IncrementTest(unittest.TestCase):
    """test the increment function"""

    def test_increment4(self):
        """test incrementing 4"""
        self.assertEqual(increment(4), 5)


if __name__ == '__main__':
    unittest.main()
