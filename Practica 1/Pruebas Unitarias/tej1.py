import sys
sys.path.insert(1, './../Ejercicios/regex')
from funs import *
import unittest

class Testcf(unittest.TestCase):
    def test_tc1(self):
        self.assertEqual(ej1("0"), "NO ES UNA IP")
    def test_tc2(self):
        self.assertEqual(ej1("1231231232"), "NO ES UNA IP")
    def test_tc3(self):
        self.assertEqual(ej1("0.1.2."), "NO ES UNA IP")
    def test_tc4(self):
        self.assertEqual(ej1("1.2.3.4"), "SI ES UNA IP")
    def test_tc5(self):
        self.assertEqual(ej1("299.299.299.299"), "SI ES UNA IP")
    def test_tc6(self):
        self.assertEqual(ej1("0.0.0.0"), "SI ES UNA IP")

if __name__ == '__main__':
    unittest.main()
