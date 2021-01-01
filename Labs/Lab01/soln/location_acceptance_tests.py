import unittest
from location import *

__unittest = True

class TestLab1(unittest.TestCase):

    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name,"SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

    def test_equal(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SF", 35.3, -120.7)
        loc4 = Location("SLO", 100, -120.7)
        loc5 = Location("SLO", 35.3, 100)
        self.assertEqual(loc1, loc2)
        self.assertNotEqual(loc1, loc3)
        self.assertNotEqual(loc1, loc4)
        self.assertNotEqual(loc1, loc5)

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        str1 = "Location('SLO', 35.3, -120.7)"
        str2 = "Location(SLO, 35.3, -120.7)"
        res = repr(loc)
        self.assertTrue(res == str1 or res == str2)

if __name__ == "__main__":
        unittest.main()
