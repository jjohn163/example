import unittest
from lab1 import *
import sys

__unittest = True

class TestLab1(unittest.TestCase):

    # Verify that max_list_itr is NOT recursive
    def check_max_list_itr(self):
        sys.setrecursionlimit(100)
        temp = []
        for val in range(200):
            temp.append(val)
        max_list_iter(temp)
        sys.setrecursionlimit(1000)
        
    # Verify that the reverse_rec function is really recursive
    def check_reverse_recursive(self):
        sys.setrecursionlimit(100)
        temp = []
        for val in range(200):
            temp.append(val)
        with self.assertRaises(RecursionError):
            reverse_rec(temp)
        sys.setrecursionlimit(1000)
   
    # Verify that the reverse_rec function is really recursive
    def check_bin_search_depth(self):
        sys.setrecursionlimit(100)
        temp = []
        for val in range(1000):
            temp.append(val)
        bin_search(4, 0, len(temp)-1, temp)
        sys.setrecursionlimit(1000)
   
    def test_max_list_iter_01(self):
        self.check_max_list_itr()  # Make sure function is iterative
        tlist = [10, 9, 8 ,4, 9]
        self.assertEqual(max_list_iter(tlist),10)
        
    def test_max_list_iter_02(self):
        self.check_max_list_itr()  # Make sure function is iterative
        tlist = [-2, 5, 8, 4, 9]
        self.assertEqual(max_list_iter(tlist), 9)
        
    def test_max_list_iter_03(self):
        self.check_max_list_itr()  # Make sure function is iterative
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)
        
    def test_max_list_iter_04(self):
        self.check_max_list_itr()  # Make sure function is iterative
        tlist = [-10, -9, -4, -12]
        self.assertEqual(max_list_iter(tlist), -4)
        
    def test_max_list_iter_05(self):
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            max_list_iter(tlist)

    def test_reverse_rec_01(self):
        self.check_reverse_recursive()
        orig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        reversed = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(reverse_rec(orig), reversed)
        
    def test_reverse_rec_02(self):
        self.check_reverse_recursive()
        orig = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        reversed = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(reverse_rec(orig), reversed)
        
    def test_reverse_rec_03(self):
        self.check_reverse_recursive()
        orig = [1]
        reversed = [1]
        self.assertEqual(reverse_rec(orig), reversed)
        
    def test_reverse_rec_04(self):
        self.check_reverse_recursive()
        orig = []
        reversed = []
        self.assertEqual(reverse_rec(orig), reversed)
        
    def test_reverse_rec_05(self):
        self.check_reverse_recursive()
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_reverse_rec_06(self):
        sys.setrecursionlimit(3000)
        orig =[]
        reversed = []
        for val in range(2000):
            orig.append(val)
            reversed.append(2000 - 1 - val)
        self.assertEqual(reverse_rec(orig[:]), reversed)
        orig.append(2000)
        self.assertEqual(reverse_rec(orig), [2000] + reversed)
        
    def test_bin_search_00(self):
        self.check_bin_search_depth()
        self.assertRaises(ValueError, bin_search, 1, 0, 5, None)
        
    def test_bin_search_01(self):
        self.check_bin_search_depth()
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)
        self.assertEqual(bin_search(0, low, high, list_val), 0)
        self.assertEqual(bin_search(10, low, high, list_val), 8)
        
    def test_bin_search_02(self):
        self.check_bin_search_depth()
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, low, high, list_val), None)
        self.assertEqual(bin_search(-5, low, high, list_val), None)
        self.assertEqual(bin_search(15, low, high, list_val), None)

    def test_bin_search_03(self):
        self.check_bin_search_depth()
        list_val =[1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 0)
        self.assertEqual(bin_search(5, low, high, list_val), None)
        self.assertEqual(bin_search(-5, low, high, list_val), None)

    def test_bin_search_04(self):
        self.check_bin_search_depth()
        list_val =[]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), None)

    def test_bin_search_05(self):
        list_val =[]
        for val in range(0, 100000, 2):
            list_val.append(val)
        low = 0
        high = len(list_val)-1
        for val in range(0, 100000, 2):        
            self.assertEqual(bin_search(val, low, high, list_val), val//2)
            self.assertEqual(bin_search(val+1, low, high, list_val), None)
            
if __name__ == "__main__":
        unittest.main()

    
