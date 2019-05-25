#!/usr/bin/python3
"""
    Test for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unitest.TestCase):
    """
        testing class
    """
    def test_basic(self):
        self.assertEqual(max_integer([2, 4, 6, 100, 0, -1, 40]), 100):
    
    def test_null(self):
        self.assertEqual(max_integer([None]), None)

    def test_empty(self):
        self.assertEqual(max_integer())

    def test_mixed(self):
        with self.assertRaises(TypeError):
            max_integer(["no", 2, 4, 5, 5.6, -20])
        with self.assertRaises(TypeError):
            max_integer(["no", 2, "4", 5, 43.3, -20.6])

if __name__ == "__main__":
    unittest.main()