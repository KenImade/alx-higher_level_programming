#!/usr/bin/python3
"""Unittests for Square class
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Defines unit tests for Square class"""

    def test_initialization(self):
        s1 = Square(5)
        s2 = Square(8)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s2.id, 6)


if __name__ == '__main__':
    unittest.main()
