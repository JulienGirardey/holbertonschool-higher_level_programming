#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_duplicates(self):
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_one_float(self):
        self.assertEqual(max_integer([2.5]), 2.5)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_reverse_sorted_list(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

if __name__ == '__main__':
    unittest.main()
