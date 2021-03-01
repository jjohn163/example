import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01_empty_table(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.get_num_items(), 0)
        self.assertAlmostEqual(ht.get_load_factor(), 0)
        self.assertEqual(ht.get_all_keys(), [])
        self.assertEqual(ht.in_table("cat"), False)
        self.assertEqual(ht.get_value("cat"), None)
        self.assertEqual(ht.get_index("cat"), None)

    def test_02_one_item(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.get_num_items(), 1)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)
        self.assertEqual(ht.get_all_keys(), ["cat"])
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.get_value("cat"), [5])
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03_multiple_same_key(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 10)
        ht.insert("cat", 15)
        ht.insert("cat", 20)
        self.assertEqual(ht.get_index("cat"), 3)
        self.assertEqual(ht.get_value("cat"), [5, 10, 15, 20])
        self.assertEqual(ht.get_num_items(), 1)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 7)

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 10)
        ht.insert("cat", 15)
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", 8)
        ht.insert("dog", 10)
        ht.insert("dog", 12)
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", 10)
        ht.insert("mouse", 11)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", 12) # hash table should be resized
        ht.insert("elephant", 13) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])
    
    def test_05_quad_wrap_around(self):
        table = HashTable(211)

        for i in range(10, 101):
            table.insert(chr(i), 10*i)
        key = chr(1) + 'E'
        table.insert(key, 'cat') # Hashes to 100, goes to 101
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 101)
        self.assertEqual(table.get_value(key), ['cat'])
        
        key = chr(2) + '&'
        table.insert(key, 'dog') # Hashes to 100, goes to 104
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 104)
        self.assertEqual(table.get_value(key), ['dog'])
        
        key = chr(3) + chr(7)
        table.insert(key, 'elephant') # Hashes to 100, goes to 109
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 109)
        self.assertEqual(table.get_value(key), ['elephant'])        

        key = chr(0) + 'd'
        table.insert(key, 'mouse') # Hashes to 100, goes to 116
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 116)
        self.assertEqual(table.get_value(key), ['mouse'])        

    def test_06_quad_wrap_around_rehash(self):
        table = HashTable(10)

        key = chr(32)
        table.insert(key, 'cat') # Hashes to 2, goes to 2
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 2)
        self.assertEqual(table.get_value(key), ['cat'])
        self.assertEqual(table.get_num_items(), 1)
        self.assertEqual(table.get_load_factor(), 1/10)

        key = chr(42)
        table.insert(key, 'dog') # Hashes to 2, goes to 3
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 3)
        self.assertEqual(table.get_value(key), ['dog'])
        self.assertEqual(table.get_num_items(), 2)
        self.assertEqual(table.get_load_factor(), 2/10)

        key = chr(52)
        table.insert(key, 'elephant') # Hashes to 2, goes to 6
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 6)
        self.assertEqual(table.get_value(key), ['elephant'])
        self.assertEqual(table.get_num_items(), 3)
        self.assertEqual(table.get_load_factor(), 3/10)

        key = chr(62)
        table.insert(key, 'mouse') # Hashes to 2, goes to 1
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 1)
        self.assertEqual(table.get_value(key), ['mouse'])
        self.assertEqual(table.get_num_items(), 4)
        self.assertEqual(table.get_load_factor(), 4/10)

        key = chr(72)
        table.insert(key, 'lion') # Hashes to 2, goes to 8
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 8)
        self.assertEqual(table.get_value(key), ['lion'])
        self.assertEqual(table.get_num_items(), 5)
        self.assertEqual(table.get_load_factor(), 5/10)

        key = chr(82)
        table.insert(key, 'tiger') # Hashes to 2, goes to 19
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 19)
        self.assertEqual(table.get_value(key), ['tiger'])
        self.assertEqual(table.get_num_items(), 6)
        self.assertEqual(table.get_load_factor(), 6/21)

    def test_07_big_oh(self):
        table = HashTable(100001)
        file = open('dictionary_a-c.txt', 'r')
        n = 0
        for line in file:
            word = line.strip()
            n += 1
            table.insert(word, word)
            self.assertTrue(table.in_table(word))
            table.get_index(word)
            self.assertEqual(table.get_value(word), [word])
            self.assertEqual(table.get_num_items(), n)
            table.get_load_factor()
        file.close()

if __name__ == '__main__':
   unittest.main()
