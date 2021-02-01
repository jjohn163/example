import unittest
from ordered_list import *
import sys

class TestLab4(unittest.TestCase):

    def test_01_init(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())

    def test_02_add(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        t_list.add(20)
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        self.assertEqual(t_list.size(), 2)
        t_list.add(30)
        self.assertEqual(t_list.python_list(), [10, 20, 30])
        self.assertEqual(t_list.size(), 3)
        t_list.add(5)
        self.assertEqual(t_list.python_list(), [5, 10, 20, 30])
        self.assertEqual(t_list.size(), 4)
        t_list.add(15)
        self.assertEqual(t_list.python_list(), [5, 10, 15, 20, 30])
        self.assertEqual(t_list.python_list_reversed(), [30, 20, 15, 10, 5])
        self.assertEqual(t_list.size(), 5)

    def test_03_remove(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(5))
        self.assertEqual(t_list.size(), 0)
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertFalse(t_list.remove(5))
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(t_list.size(), 5)
        self.assertFalse(t_list.remove(55))
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(t_list.size(), 5)
        self.assertTrue(t_list.remove(40))
        self.assertEqual(t_list.python_list(), [10, 20, 30, 50])
        self.assertEqual(t_list.size(), 4)
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.python_list(), [20, 30, 50])
        self.assertEqual(t_list.size(), 3)
        self.assertTrue(t_list.remove(50))
        self.assertEqual(t_list.python_list(), [20, 30])
        self.assertEqual(t_list.size(), 2)
        self.assertTrue(t_list.remove(20))
        self.assertEqual(t_list.python_list(), [30])
        self.assertEqual(t_list.size(), 1)
        self.assertTrue(t_list.remove(30))
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)

    def test_04_index(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(20), 1)
        self.assertEqual(t_list.index(30), 2)
        self.assertEqual(t_list.index(40), 3)
        self.assertEqual(t_list.index(50), 4)
        self.assertEqual(t_list.index(5), None)
        self.assertEqual(t_list.index(55), None)
        self.assertEqual(t_list.index(25), None)

    def test_05_pop(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertRaises(IndexError, t_list.pop, -1)
        self.assertEqual(t_list.size(), 5)
        self.assertRaises(IndexError, t_list.pop, 5)
        self.assertEqual(t_list.size(), 5)
        self.assertEqual(t_list.pop(0), 10)
        self.assertEqual(t_list.python_list(), [20, 30, 40, 50])
        self.assertEqual(t_list.python_list_reversed(), [50, 40, 30, 20])
        self.assertEqual(t_list.size(), 4)
        self.assertEqual(t_list.pop(3), 50)
        self.assertEqual(t_list.python_list(), [20, 30, 40])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.pop(1), 30)
        self.assertEqual(t_list.python_list(), [20, 40])
        self.assertEqual(t_list.size(), 2)
        self.assertEqual(t_list.pop(0), 20)
        self.assertEqual(t_list.python_list(), [40])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.pop(0), 40)
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())

    def test_06_search(self):
        t_list = OrderedList()
        self.assertFalse(t_list.search(10))
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(20))
        self.assertTrue(t_list.search(30))
        self.assertTrue(t_list.search(40))
        self.assertTrue(t_list.search(50))
        self.assertFalse(t_list.search(5))
        self.assertFalse(t_list.search(55))
        self.assertFalse(t_list.search(25))

    def test_07_python_list(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(),[])
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.python_list_reversed(), [10])
        t_list.add(20)
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(t_list.python_list_reversed(), [50, 40, 30, 20, 10])

    def test_08_size_is_empty(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(),0)
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        t_list.add(20)
        self.assertEqual(t_list.size(), 2)
        self.assertFalse(t_list.is_empty())
        t_list.remove(20)
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        t_list.remove(10)
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())
        t_list.remove(10)
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())

        t_list.add(10)
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        t_list.add(20)
        self.assertEqual(t_list.size(), 2)
        self.assertFalse(t_list.is_empty())
        t_list.pop(0)
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        t_list.pop(0)
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())

    def test_09_add_remove_all_add(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(200):
            self.assertTrue(t_list.remove(val))
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.size(), 0)
        for val in range(200):
            t_list.add(val)
        self.assertEqual(t_list.size(), 200)
        self.assertFalse(t_list.is_empty())

    def test_10_add_pop_all_add(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(199, -1, -1):
            self.assertEqual(t_list.pop(val), val)
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.size(), 0)
        for val in range(200):
            t_list.add(val)
        self.assertEqual(t_list.size(), 200)
        self.assertFalse(t_list.is_empty())

    def test_11_add_pop_remove(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(100):
            self.assertEqual(t_list.pop(0), val)
            self.assertTrue(t_list.remove(199-val))
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.size(), 0)
        for val in range(200):
            t_list.add(val)
        self.assertEqual(t_list.size(), 200)
        self.assertFalse(t_list.is_empty())
        for val in range(100):
            self.assertEqual(t_list.pop(199 - 2*val), 199-val)
            self.assertTrue(t_list.remove(val))
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.size(), 0)

    # Recursive checks repeated below to cause multiple deductions if code not recursive
    def test_12_size_is_recursive01(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.size()
        sys.setrecursionlimit(1000)

    def test_13_search_is_recursive01(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.search(175)
        sys.setrecursionlimit(1000)

    def test_14_python_list_reversed_is_recursive01(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.python_list_reversed()
        sys.setrecursionlimit(1000)

    def test_15_size_is_recursive02(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.size()
        sys.setrecursionlimit(1000)

    def test_16_search_is_recursive02(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.search(175)
        sys.setrecursionlimit(1000)

    def test_17_python_list_reversed_is_recursive02(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.python_list_reversed()
        sys.setrecursionlimit(1000)

    def test_18_search_is_recursive03(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.search(175)
        sys.setrecursionlimit(1000)

    def test_19_python_list_reversed_is_recursive03(self):
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        sys.setrecursionlimit(150)
        with self.assertRaises(RecursionError):
            t_list.python_list_reversed()
        sys.setrecursionlimit(1000)

if __name__ == '__main__': 
    unittest.main()
