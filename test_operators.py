#!/usr/bin/env python3

# test_operators.py
import unittest
from operators import demonstrate_operators

class TestOperators(unittest.TestCase):
    def test_demonstrate_operators(self):
        # This is a simple test case to ensure that the function runs without errors.
        try:
            demonstrate_operators()
            success = True
        except Exception as e:
            success = False
        self.assertTrue(success, "demonstrate_operators() function failed.")

if __name__ == "__main__":
    unittest.main()
