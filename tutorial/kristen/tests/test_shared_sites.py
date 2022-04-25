# imports
import unittest
import sys, os, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from scripts import shared_sites

class TestSharedSites(unittest.TestCase):
    q1 = [0, 0, 0, 0, 0]
    q2 = [1, 1, 1, 1, 1]
    q3 = [0, 1, 0, 1, 2]
    m1 = [0, 0, 0, 0, 0]
    m2 = [1, 1, 1, 1, 1]
    m3 = [2, 2, 2, 2, 2]

    def test_count_shared_sites(self):
        self.assertEqual(shared_sites.count_shared_sites(self.q1, self.m1), 5)
        self.assertEqual(shared_sites.count_shared_sites(self.q1, self.m2), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q1, self.m3), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q2, self.m1), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q2, self.m2), 5)
        self.assertEqual(shared_sites.count_shared_sites(self.q2, self.m3), 0)
        self.assertEqual(shared_sites.count_shared_sites(self.q3, self.m1), 2)
        self.assertEqual(shared_sites.count_shared_sites(self.q3, self.m2), 2)
        self.assertEqual(shared_sites.count_shared_sites(self.q3, self.m3), 1)

    def test_percent_shared_sites(self):
        self.assertEqual(shared_sites.percent_shared_sites(self.q1, self.m1), 0.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q1, self.m2), 1.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q1, self.m3), 1.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q2, self.m1), 1.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q2, self.m2), 0.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q2, self.m3), 1.)
        self.assertEqual(shared_sites.percent_shared_sites(self.q3, self.m1), 0.6)
        self.assertEqual(shared_sites.percent_shared_sites(self.q3, self.m2), 0.6)
        self.assertEqual(shared_sites.percent_shared_sites(self.q3, self.m3), 0.8)

class TestIndexedMatches(unittest.TestCase):
    db = [[0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2],
           [3, 3, 3, 3, 3],
           [4, 4, 4, 4, 4]]
    q1 = [[0, 0, 0, 0, 0]]
    i1 = [[0, 1, 2]]
    m1 = [[0., 1., 1.]]
    q2 = [[1, 1, 1, 0, 0]]
    i2 = [[1, 0, 2]]
    m2 = [[0.4, 0.6, 1.]]
    q3 = [[0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1],
          [2, 2, 2, 2, 2]]
    i3 = [[0, 1, 2],
          [1, 2, 0],
          [2, 3, 1]]
    m3 = [[0., 1., 1.],
          [0., 1., 1.],
          [0., 1., 1.]]

    def test_all_indexed_matches(self):
        self.assertEqual(shared_sites.
                         all_indexed_matches(self.q1, self.i1, self.db), self.m1)
        self.assertEqual(shared_sites.
                         all_indexed_matches(self.q2, self.i2, self.db), self.m2)
        self.assertEqual(shared_sites.
                         all_indexed_matches(self.q3, self.i3, self.db), self.m3)

class TestAllDatabase(unittest.TestCase):
    db = [[0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1],
          [2, 2, 2, 2, 2],
          [3, 3, 3, 3, 3],
          [4, 4, 4, 4, 4]]
    q1 = [[0, 0, 0, 0, 0]]
    q2 = [[1, 1, 1, 1, 1]]
    q3 = [[0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1],
          [2, 2, 2, 2, 2]]
    q4 = [[0, 0, 1, 1, 2]]
    m1 = [[0., 1., 1., 1., 1.]]
    m2 = [[1., 0., 1., 1., 1.]]
    m3 = [[0., 1., 1., 1., 1.],
          [1., 0., 1., 1., 1.],
          [1., 1., 0., 1., 1.]]
    m4 = [[0.6, 0.6, 0.8, 1., 1.]]
    def test_percent_shared_sites(self):
        self.assertEqual(shared_sites.all_database(self.q1, self.db), self.m1)
        self.assertEqual(shared_sites.all_database(self.q2, self.db), self.m2)
        self.assertEqual(shared_sites.all_database(self.q3, self.db), self.m3)
        self.assertEqual(shared_sites.all_database(self.q4, self.db), self.m4)

class TestAccuracyIndices(unittest.TestCase):
    m1 = [[0., 1., 1., 1., 1.]]
    m2 = [[1., 0., 1., 1., 1.]]
    m3 = [[0., 1., 1., 1., 1.],
          [1., 0., 1., 1., 1.],
          [1., 1., 0., 1., 1.]]
    m4 = [[0.6, 0.6, 0.8, 1., 1.]]

    def test_accuracy_indices(self):
        self.assertIsNone(np.testing.assert_array_equal(
            shared_sites.accuracy_indices(self.m1), [[0, 1, 2, 3, 4]]))
        self.assertIsNone(np.testing.assert_array_equal(
            shared_sites.accuracy_indices(self.m2), [[1, 0, 2, 3, 4]]))
        self.assertIsNone(np.testing.assert_array_equal(
            shared_sites.accuracy_indices(self.m3), [[0, 1, 2, 3, 4],
                                                     [1, 0, 2, 3, 4],
                                                     [2, 0, 1, 3, 4]]))
        self.assertIsNone(np.testing.assert_array_equal(
            shared_sites.accuracy_indices(self.m1), [[0, 1, 2, 3, 4]]))

class TestSSvsBF(unittest.TestCase):
    ss1 = [0, 1, 2, 3, 4]
    ss2 = [1, 2, 0, 3, 4]
    bf1 = [0, 1, 2, 3, 4]
    bf2 = [1, 2, 0, 3, 4]
    def test_ss_vs_bf(self):
        self.assertEqual(shared_sites.ss_vs_bf(self.ss1, self.bf1, 1), True)
        self.assertEqual(shared_sites.ss_vs_bf(self.ss1, self.bf1, 2), True)
        self.assertEqual(shared_sites.ss_vs_bf(self.ss1, self.bf1, 5), True)
        self.assertEqual(shared_sites.ss_vs_bf(self.ss2, self.bf2, 1), True)
        self.assertEqual(shared_sites.ss_vs_bf(self.ss2, self.bf2, 2), True)
        self.assertEqual(shared_sites.ss_vs_bf(self.ss2, self.bf2, 5), True)
        self.assertEqual(shared_sites.ss_vs_bf(self.ss1, self.bf2, 1), False)
        self.assertEqual(shared_sites.ss_vs_bf(self.ss1, self.bf2, 4), False)

if __name__ == '__main__':
    unittest.main()
