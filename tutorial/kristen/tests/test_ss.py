# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import sample_major_format



class TestFAISS(unittest.TestCase):
    # INPUTS FOR TESTING
    db1 = [[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4]]
    q1 = [0, 0, 0, 0, 0]


    def test_get_data_type(self):
        self.assertEqual(similarity_search.similarity_search(self.db1, self.q1, 1), [0])

if __name__ == '__main__':
    unittest.main()
