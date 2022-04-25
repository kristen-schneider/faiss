# imports
import unittest
import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import numpy as np
from scripts import sample_major_format


class TestSampleMajorFormat(unittest.TestCase):
    db1 = [[0, 0, 0, 0, 0]]
    db2 = [[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4]]
    smf1 = [[0], [0], [0], [0], [0]]
    smf2 = [[0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4],
            [0, 1, 2, 3, 4]]

    def test_transpose_data(self):
        self.assertEqual(sample_major_format.transpose_data(self.db1), self.smf1)
        self.assertEqual(sample_major_format.transpose_data(self.db2), self.smf2)
        self.assertNotEqual(sample_major_format.transpose_data(self.db1), self.smf2)

if __name__ == '__main__':
    unittest.main()