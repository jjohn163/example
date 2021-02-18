import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_00_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_01_selection_sort_sorts(self):
        sizes = [250, 500, 1000, 1500]
        random.seed(1234)
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            selection_sort(randoms)
            self.assertEqual(randoms, expected)
            
    def test_02_insertion_sort_sorts(self):
        sizes = [250, 500, 1000, 1500]
        random.seed(1234)
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            insertion_sort(randoms)
            self.assertEqual(randoms, expected)
            
    def test_03_selection_sort_number_of_comps(self):
        sizes = [250, 500, 1000, 1500]
        random.seed(1234)
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            comps = selection_sort(randoms)
            self.assertEqual(comps, n*(n-1)/2)
            
    def test_04_insertion_sort_number_of_comps(self):
        n = 1000
        random.seed(1234)
        randoms = random.sample(range(1000000), n)
        comps = insertion_sort(randoms)
        self.assertTrue(comps > 200000)
        comps = insertion_sort(randoms)
        self.assertEqual(comps, 999)
            
    def test_05_insertion_sort_number_of_comps_sorted_list(self):
        n = 1000
        random.seed(1234)
        randoms = random.sample(range(1000000), n)
        randoms.sort()
        comps = insertion_sort(randoms)
        self.assertEqual(comps, 999)

    def test_06_selection_sort_sorts_small(self):
        sizes = [5, 10, 15]
        random.seed(1234)
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            selection_sort(randoms)
            self.assertEqual(randoms, expected)
            
    def test_07_selection_sort_sorts_reversed(self):
        sizes = [250, 500, 1000, 1500]
        random.seed(1234)
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            randoms.sort()
            expected = list(randoms)
            randoms.sort(reverse=True)
            selection_sort(randoms)
            self.assertEqual(randoms, expected)
            
    def test_08_insertion_sort_sorts_small(self):
        sizes = [5, 10, 15]
        random.seed(1234)
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            insertion_sort(randoms)
            self.assertEqual(randoms, expected)
            
    def test_09_insertion_sort_sorts_reversed(self):
        sizes = [250, 500, 1000, 1500]
        random.seed(1234)
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            randoms.sort()
            expected = list(randoms)
            randoms.sort(reverse=True)
            insertion_sort(randoms)
            self.assertEqual(randoms, expected)                    

if __name__ == '__main__': 
    unittest.main()
