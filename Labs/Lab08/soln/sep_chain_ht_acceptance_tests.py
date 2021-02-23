
import unittest
from sep_chain_ht import *

class TestList(unittest.TestCase):

   def test_insert1(self):
      hash1 = MyHashTable()
      hash1.insert(11, "a") 
      hash1.insert(3, "b")
      hash1.insert(1, "c") 
      hash1.insert(8, "d") 
      hash1.insert(4, "e") 
      hash1.insert(5, "f") 
      hash1.insert(2, "h") 
      self.assertEqual(hash1.size(), 7)
      

   def test_insert2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d") 
      hash1.insert(4, "e")
      hash1.insert(5, "f") 
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      hash1.insert(0, "rehash")
      hash1.insert(6, "i")
      self.assertEqual(hash1.size(), 9)
      

   def test_get1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")

      self.assertEqual(hash1.get(1), (1, 'g'))
      self.assertEqual(hash1.get(2), (2, 'h'))
      self.assertEqual(hash1.get(3), (3, 'b'))
      self.assertEqual(hash1.get(4), (4, 'e'))
      self.assertEqual(hash1.get(5), (5, 'f'))
      self.assertEqual(hash1.get(8), (8, 'd'))
      self.assertEqual(hash1.get(11), (11, 'a'))

      self.assertEqual(hash1.size(), 7)
      
   def test_get2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      with self.assertRaises(LookupError):
            hash1.get(6)

   def test_remove1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      
      self.assertEqual(hash1.remove(1), (1, 'g'))
      self.assertEqual(hash1.remove(2), (2, 'h'))
      self.assertEqual(hash1.remove(3), (3, 'b'))
      self.assertEqual(hash1.remove(4), (4, 'e'))
      self.assertEqual(hash1.remove(5), (5, 'f'))
      self.assertEqual(hash1.remove(8), (8, 'd'))
      self.assertEqual(hash1.remove(11), (11, 'a'))

      self.assertEqual(hash1.size(), 0)
      
   def test_remove2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      with self.assertRaises(LookupError):
            hash1.remove(5)

   def test_size1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(6, "g")
      self.assertEqual(hash1.size(), 7)

   def test_size2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      self.assertEqual(hash1.size(), 6)

   def test_size3(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.remove(3)
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      self.assertEqual(hash1.size(), 4)

   def test_load_factor1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      self.assertEqual(hash1.load_factor(), 1.4)

   def test_load_factor2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      hash1.insert(0, "rehash")
      hash1.insert(6, "i")
      self.assertAlmostEqual(hash1.load_factor(), 0.8181818)

if __name__ == '__main__': 
   unittest.main()
   