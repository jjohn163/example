import unittest
import filecmp
import subprocess
from concordance import *

class TestList(unittest.TestCase):

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        #self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))
        err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        #self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))
        err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        #self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))
        err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("dictionary_a-c.txt")
        conc.write_concordance("dictionary_a-c_con.txt")
        #self.assertTrue(filecmp.cmp("dictionary_a-c_con.txt", "dictionary_a-c_sol.txt"))
        err = subprocess.call("diff -wb dictionary_a-c_con.txt dictionary_a-c_sol.txt", shell = True)
        self.assertEqual(err, 0)
        
    def test_05(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("stop_words.txt")
        conc.write_concordance("stop_words_con.txt")
        #self.assertTrue(filecmp.cmp("stop_words_con.txt", "stop_words_sol.txt"))
        err = subprocess.call("diff -wb stop_words_con.txt stop_words_sol.txt", shell = True)
        self.assertEqual(err, 0)


if __name__ == '__main__':
   unittest.main()
