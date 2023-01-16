#!/usr/bin/python3
"""Unittests for Rectangle"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.Rectangle):
    """Defines unit tests for Rectangle class"""

    def test_initialization(self):
        r1 = Rectangle(3, 6)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)
        r2 = Rectangle(2, 5)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)


if __name__ == "__main__":
    unittest.main()
