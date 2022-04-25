# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import similarity_search


class TestFAISS(unittest.TestCase):
    # INPUTS FOR TESTING
    db1 = [[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4]]
    q1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    q2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
    q3 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2]]

    def test_ss_k1(self):
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q1, 1),
            [[0], [0]]))
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q2, 1),
            [[0], [1]]))
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q3, 1),
            [[0], [1], [2]]))

    def test_ss_k2(self):
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q1, 2),
            [[0, 1], [0, 1]]))
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q2, 2),
            [[0, 1], [1, 0]]))
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q3, 2),
            [[0, 1], [1, 0], [2, 1]]))

    def test_ss_k5(self):
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q1, 5),
            [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]))
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q2, 5),
            [[0, 1, 2, 3, 4], [1, 2, 0, 3, 4]]))
        self.assertIsNone(np.testing.assert_array_equal(
            similarity_search.similarity_search(self.db1, self.q3, 5),
            [[0, 1, 2, 3, 4], [1, 2, 0, 3, 4], [2, 1, 3, 4, 0]]))


if __name__ == '__main__':
    unittest.main()
