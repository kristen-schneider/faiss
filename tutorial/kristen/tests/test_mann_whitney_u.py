# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import mann_whitney_u

class TestMannWhitneyUSmall(unittest.TestCase):
    group1 = [1, 2, 3, 4, 5]
    group2 = [1, 2, 3, 4, 5]
    group3 = [5, 4, 3, 2, 1]
    group4 = [0, 0, 0, 0, 0]
    group5 = [6, 7, 8, 9, 10]
    group6 = [2, 4, 5, 1, 3]
    random1 = np.random.randint(500, size=(100, 31))

    def test_accept_null(self):
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group1, self.group2)[1], 1)
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group1, self.group3)[1], 1)
        self.assertEqual(mann_whitney_u.mann_whitney_u_test(self.group2, self.group3)[1], 1)
        self.assertGreaterEqual(mann_whitney_u.mann_whitney_u_test(self.group1, self.group6)[1], 1)


# class TestMannWhitneyUGenotypes(unittest.TestCase):
#     group1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     group2 = [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
#     group3 = [0, 0, 2, 1, 0, 0, 0, 2, 0, 0]
#     group4 = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]
#     group5 = [0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
#
#     print(mann_whitney_u.mann_whitney_u_test(group1, group2))
#     print(mann_whitney_u.mann_whitney_u_test(group1, group3))
#     print(mann_whitney_u.mann_whitney_u_test(group1, group4))
#     print(mann_whitney_u.mann_whitney_u_test(group1, group5))
#     # print(mann_whitney_u.mann_whitney_u_test(group3, group5))





if __name__ == '__main__':
    unittest.main()