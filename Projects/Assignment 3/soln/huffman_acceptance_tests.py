import unittest
import filecmp
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
      freqlist	= cnt_freq("file2.txt")
      anslist = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist)


    def test_create_huff_tree(self):
      freqlist = cnt_freq("file2.txt")
      hufftree = create_huff_tree(freqlist)
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 97)
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 97)
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 100)

    def test_create_header(self):
      freqlist = cnt_freq("file2.txt")
      self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
      freqlist = cnt_freq("file2.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
      huffman_encode("file1.txt", "file1_out.txt")
      # capture errors by running 'filecmp' on your encoded file with a *known* solution file
      self.assertTrue(filecmp.cmp("file1_out.txt", "file1_soln.txt"))

    def test_02_textfile(self):
      huffman_encode("file2.txt", "file2_out.txt")
      # capture errors by running 'filecmp' on your encoded file with a *known* solution file
      self.assertTrue(filecmp.cmp("file2_out.txt", "file2_soln.txt"))

    def test_03_textfile(self):
      huffman_encode("multiline.txt", "multiline_out.txt")
      # capture errors by running 'filecmp' on your encoded file with a *known* solution file
      self.assertTrue(filecmp.cmp("multiline_out.txt", "multiline_soln.txt"))

    def test_04_textfile(self):
      huffman_encode("declaration.txt", "declaration_out.txt")
      # capture errors by running 'filecmp' on your encoded file with a *known* solution file
      self.assertTrue(filecmp.cmp("declaration_out.txt", "declaration_soln.txt"))
      huffman_decode("declaration_out.txt", "declaration_decode.txt")
      self.assertTrue(filecmp.cmp("declaration.txt", "declaration_decode.txt"))

if __name__ == '__main__': 
   unittest.main()
