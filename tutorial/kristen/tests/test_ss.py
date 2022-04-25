# imports
import unittest
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import numpy as np

class TestFAISS(unittest.TestCase):
    # INPUTS FOR TESTING
    db1 = [[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4]]
    q1 = [0, 0, 0, 0, 0]

    def test_get_data_type(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
