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





# class TestPercentSharedSites(unittest.TestCase):
#     def test_percent_shared_sites(self):




if __name__ == '__main__':
    unittest.main()
