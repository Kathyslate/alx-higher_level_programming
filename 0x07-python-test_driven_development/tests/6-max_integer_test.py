#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integerempty_list(self):
        """utitTest with a empty list: will return None"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
        """utitTest with a non-empty range list: will return a value """
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_multiple_elements(self):
        """utitTest with a non-empty given list: will return a value """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_negative_numbers(self):
        """utitTest with a non-empty negative given list: will return a value """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_max_integer_mixed_numbers(self):
        """utitTest with a non-empty mixed given list: will return a value """
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

if __name__ == '__main__':
    unittest.main()
