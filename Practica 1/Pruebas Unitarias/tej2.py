import sys
sys.path.insert(1, './../Ejercicios/regex')
from funs import *
import unittest

class Testcf(unittest.TestCase):
    def test_tc1(self):
        self.assertEqual(ej2("012345abc"), "NO ES UNA VARIABLE")
    def test_tc2(self):
        self.assertEqual(ej2("Escanor x 2"), "NO ES UNA VARIABLE")
    def test_tc3(self):
        self.assertEqual(ej2("121.10.200.3 "), "NO ES UNA VARIABLE")
    def test_tc4(self):
        self.assertEqual(ej2("mynameiscamila"), "SI ES UNA VARIABLE")
    def test_tc5(self):
        self.assertEqual(ej2("Var21314"), "SI ES UNA VARIABLE")
    def test_tc6(self):
        self.assertEqual(ej2("__myvar__"), "SI ES UNA VARIABLE")

if __name__ == '__main__':
    unittest.main()
