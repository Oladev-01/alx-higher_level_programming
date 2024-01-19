#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class test for each unittest of
      the function max_integer([...])"""

    def test_max_with_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -3, -3, -2]), -1)
        self.assertEqual(max_integer([1.5, 2.5, -6.5, -7.5]), 2.5)
        self.assertEqual(max_integer([10]), 10)

    def test_char_with_int(self):
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer([1, 2, "a", "A", 15]))
            self.assertEqual(max_integer(["string", "integer"]))
            self.assertEqual(max_integer(["a", 1, "srting", 'c']))
            self.assertEqual(max_integer(['a', 'b']))

    def test_for_none(self):
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
