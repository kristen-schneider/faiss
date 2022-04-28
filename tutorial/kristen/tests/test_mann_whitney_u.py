# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import mann_whitney_u

class TestMannWhitneyU(unittest.TestCase):
    group1 = [1, 2, 3, 4, 5]
    group2 = [1, 2, 3, 4, 5]
    group3 = [5, 4, 3, 2, 1]
    group4 = [0, 0, 0, 0, 0]

    def test_mann_whitney_u_pvalue(self):
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group1, self.group2)[1], 1)
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group2, self.group1)[1], 1)
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group1, self.group3)[1], 1)
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group3, self.group1)[1], 1)
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group2, self.group3)[1], 1)
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group3, self.group2)[1], 1)




if __name__ == '__main__':
    unittest.main()