import unittest
import sys
from  base_convert import *

class TestBaseConvert(unittest.TestCase):


    def test_base2_00(self):
        sys.setrecursionlimit(60)
        self.assertRaises(RecursionError,convert,2**61,2)
        sys.setrecursionlimit(1000)


    def test_base2_01(self):
        self.assertEqual(convert(2**61,2),"10000000000000000000000000000000000000000000000000000000000000")


    def test_base2_02(self):
        self.assertEqual(convert(45,2),"101101")


    def test_base2_03(self):
        self.assertEqual(convert(54321,2),"1101010000110001")


    def test_base4_01(self):
        self.assertEqual(convert(30,4),"132")


    def test_base7_01(self):
        self.assertEqual(convert(30,7),"42")


    def test_base10_01(self):
        for i in range(10000):
            self.assertEqual(convert(i, 10),str(i))


    def test_base12_01(self):
        self.assertEqual(convert(5555555,12),"1A3B02B")


    def test_base16_01(self):
        self.assertEqual(convert(316,16),"13C")


    def test_base16_02(self):
        self.assertEqual(convert(11259375,16),"ABCDEF")


    def test_base16_03(self):
        self.assertEqual(convert(324508639,16),"13579BDF")


    def test_base_all_01(self):
        for i in range(2,17):
            for j in range(0,min(i,10)):
                self.assertEqual(convert(j,i),str(j))
            for k in range(10,i):
                self.assertEqual(convert(k,i),chr(65+k-10))


    def test_base2_long(self):
        size = 2000
        digits = ['1'] + ['0' for i in range(size)]
        res = ''.join(digits)
        self.assertRaises(RecursionError,convert,2**size,2)
        sys.setrecursionlimit(size + 500)
        self.assertEqual(convert(2**size, 2),res)
        sys.setrecursionlimit(1000)

if __name__ == "__main__":
        unittest.main()