import unittest
from binary_search_tree import *
import random

class TestLab4(unittest.TestCase):

    def test_01_simple(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        #self.assertTrue(bst.delete(10))
        #self.assertEqual(bst.tree_height(), None)

    def test_02_insert_search(self):
        bst = BinarySearchTree()
        values = [99, -4, 167, 139, 55, -89, 13, 78, 128, 119]

        for val in values:
            bst.insert(val)

        for val in values:
            self.assertTrue(bst.search(val))
            self.assertFalse(bst.search(val - 1))
            self.assertFalse(bst.search(val + 1))
            
    def test_03_search_empty_list(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.search(999))

    def test_04_pre_in_level_order_empty_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])

    def test_05_test_find_min(self):
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
        data = ['stuff', None, -1000, 3, 4, 5, 6, 7, 8, 9]
      
        for i in range(len(keys)):
            bst.insert(keys[i], data[i])

            if i < 1:
                self.assertEqual((99, 'stuff'), bst.find_min())
            elif i < 5:
                self.assertEqual((-4, None), bst.find_min())
            else:
                self.assertEqual((-89, 5), bst.find_min())

    def test_06_test_find_max(self):
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
        data = ['stuff', 1000, None, 3, 4, 5, 6, 7, 8, 9]
      
        for i in range(len(keys)):
            bst.insert(keys[i], data[i])

            if i < 2:
                self.assertEqual((99, 'stuff'), bst.find_max())
            elif i < 8:
                self.assertEqual((167, None), bst.find_max())
            else:
                self.assertEqual((178, 8), bst.find_max())
                
    def test_07_test_min_max_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(None, bst.find_max())
        self.assertEqual(None, bst.find_min())

    def test_08_test_inorder(self):
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.inorder_list(), [-89, -4, 13, 55, 78, 99, 139, 167, 174, 178])

    def test_09_test_preorder(self):
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.preorder_list(), [99, -4, -89, 55, 13, 78, 167, 139, 178, 174])

    def test_09_test_level_order(self):
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.level_order_list(), [99, -4, 167, -89, 55, 139, 178, 13, 78, 174])

    '''def test_10_delete_empty(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.delete(10))

    def test_11_delete_size_1(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertFalse(bst.is_empty())
        self.assertTrue(bst.delete(10))
        self.assertTrue(bst.is_empty())
        self.assertFalse(bst.search(10))
        bst.insert(20)
        self.assertFalse(bst.is_empty())
        self.assertFalse(bst.search(10))
        self.assertFalse(bst.delete(10))
        self.assertTrue(bst.delete(20))
        self.assertFalse(bst.search(20))
        self.assertTrue(bst.is_empty())
    
    def test_12_delete_size_2_and_3(self):
        bst = BinarySearchTree()
        
        bst.insert(99)
        bst.insert(88)

        # Root first...
        self.assertTrue(bst.delete(99))
        self.assertTrue(bst.search(88))
        self.assertFalse(bst.search(99))

        bst.delete(88);
        self.assertFalse(bst.search(88))
        self.assertFalse(bst.search(99))

        # Leaf first...
        bst.insert(99)
        bst.insert(88)

        self.assertTrue(bst.delete(88))
        self.assertTrue(bst.search(99))
        self.assertFalse(bst.search(88))

        self.assertTrue(bst.delete(99))
        self.assertFalse(bst.search(88))
        self.assertFalse(bst.search(99))
        
        # Root, root, root... 
        bst.insert(88)
        bst.insert(77)
        bst.insert(99)

        self.assertTrue(bst.delete(77))
        self.assertFalse(bst.search(77))
        self.assertTrue(bst.search(88))
        self.assertTrue(bst.search(99))

        self.assertTrue(bst.delete(88))
        self.assertFalse(bst.search(77))
        self.assertFalse(bst.search(88))
        self.assertTrue(bst.search(99))

        self.assertTrue(bst.delete(99))
        self.assertFalse(bst.search(77))
        self.assertFalse(bst.search(88))
        self.assertFalse(bst.search(99))

        # Left, right, root...
        bst.insert(88)
        bst.insert(77)
        bst.insert(99)

        self.assertTrue(bst.delete(77))
        self.assertFalse(bst.search(77))
        self.assertTrue(bst.search(88))
        self.assertTrue(bst.search(99))

        self.assertTrue(bst.delete(99))
        self.assertFalse(bst.search(77))
        self.assertFalse(bst.search(99))
        self.assertTrue(bst.search(88))

        self.assertTrue(bst.delete(88))
        self.assertFalse(bst.search(77))
        self.assertFalse(bst.search(99))
        self.assertFalse(bst.search(88))

        # Right, left, root...
        bst.insert(88)
        bst.insert(77)
        bst.insert(99)

        self.assertTrue(bst.delete(99))
        self.assertFalse(bst.search(99))
        self.assertTrue(bst.search(88))
        self.assertTrue(bst.search(77))

        self.assertTrue(bst.delete(77))
        self.assertFalse(bst.search(77))
        self.assertFalse(bst.search(99))
        self.assertTrue(bst.search(88))

        self.assertTrue(bst.delete(88))
        self.assertFalse(bst.search(88))
        self.assertFalse(bst.search(77))
        self.assertFalse(bst.search(99))

    def test_13_delete_other(self):
        bst = BinarySearchTree()
        
        bst.insert(30)
        bst.insert(40)
        bst.insert(35)
        bst.insert(50)
        bst.insert(60)
        self.assertTrue(bst.delete(40))
        self.assertEqual(bst.inorder_list(), [30, 35, 50, 60])   
        
        bst = BinarySearchTree()
        bst.insert(30)
        bst.insert(20)
        bst.insert(10)
        bst.insert(25)
        bst.delete(30)
        self.assertEqual(bst.inorder_list(), [10, 20, 25])   
        bst.delete(10)
        bst.delete(20)
        bst.insert(40)
        bst.insert(30)
        bst.insert(50)
        self.assertEqual(bst.inorder_list(), [25, 30, 40, 50])   
        bst.delete(25)
        self.assertEqual(bst.inorder_list(), [30, 40, 50])   
        bst.delete(40)
        self.assertEqual(bst.inorder_list(), [30, 50])'''   
        
    def test_14_insert_replace(self):
        bst = BinarySearchTree()
        bst.insert(30, 'aaa')
        bst.insert(40, 'bbb')
        bst.insert(35, 'ccc')
        bst.insert(50, 'ddd')
        bst.insert(60, 'eee')
        bst.insert(60, 'zzz')
        self.assertEqual(bst.find_max(), (60, 'zzz'))
        self.assertEqual(bst.tree_height(), 3)
        
    def test_15_tree_of_strings(self):
        bst = BinarySearchTree()
        strings = ["Hello", "these", "are", "some", "random", "strings.", "If", "this", 
                                       "test", "fails", "it's", "likely", "because", "the", "BST", "code", "being", "tested",
                                       "uses", "operators", "other", "than", "<", ">", "and", "=="]
        sortedStrings = []
        otherStrings = ["things", "that", "do", "not", "exist", "in", "strings"]

        for i in range(len(strings)):
            sortedStrings.append(strings[i])
            bst.insert(strings[i], i)
        
        for s in strings:
            self.assertTrue(bst.search(s))
         
        for s in otherStrings:
            self.assertFalse(bst.search(s))

        sortedStrings.sort()
        self.assertEqual(sortedStrings[0], bst.find_min()[0])
        self.assertEqual(sortedStrings[len(sortedStrings)-1], bst.find_max()[0])

        self.assertEqual(bst.inorder_list(), sortedStrings)        

    def test_16_test_tree_height(self):
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])            
        self.assertEqual(bst.tree_height(), 3)

        bst = BinarySearchTree()
        keys.sort()
        for i in range(len(keys)):
            bst.insert(keys[i])
        self.assertEqual(bst.tree_height(), 9)
      
        bst = BinarySearchTree()
        keys.sort(reverse=True)
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.tree_height(), 9)
        
    def test_17_big_O_insert_search_min_max(self):
        size = 20000
        bst = BinarySearchTree()

        random.seed(1234)
        for i in range(size):
            bst.insert(random.randint(0, 1000000))
            
        bst.insert(-1, 'aaa') # Will be the min
        bst.insert(1000001, 'zzz') # Will be the max
        
        random.seed(1234)
        for i in range(size):
            self.assertTrue(bst.search(random.randint(0, 1000000)))
            self.assertEqual(bst.find_min(), (-1, 'aaa'))
            self.assertEqual(bst.find_max(), (1000001, 'zzz'))
        
    def test_18_big_O_traversals(self):
        size = 30000
        bst = BinarySearchTree()

        random.seed(1234)
        for i in range(size):
            bst.insert(random.randint(0, 1000000))
            
        for i in range(1):
            self.assertEqual(bst.tree_height(), 34)
            
            self.assertEqual(len(bst.preorder_list()), 29516)
            self.assertEqual(len(bst.inorder_list()), 29516)
            self.assertEqual(len(bst.level_order_list()), 29516)
        
if __name__ == '__main__': 
    unittest.main()
