#!/usr/bin/python3
"""Unittests for Base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Defines unit tests for Base model"""

    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_saving_id(self):
        base = Base(10)
        self.assertEqual(base.id, 10)


if __name__ == '__main__':
    unittest.main()
