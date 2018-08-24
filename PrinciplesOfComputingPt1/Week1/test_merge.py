import unittest
from merge import merge


class MergeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])

    def test_2(self):
        self.assertEqual(merge(0, 0, 2, 2), [4, 0, 0, 0])

    def test_3(self):
        self.assertEqual(merge(2, 2, 0, 0), [4, 0, 0, 0])

    def test_4(self):
        self.assertEqual(merge(2, 2, 2, 2, 2), [4, 4, 2, 0, 0])

    def test_5(self):
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])
