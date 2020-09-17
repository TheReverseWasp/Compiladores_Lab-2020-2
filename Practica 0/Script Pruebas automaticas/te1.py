import sys
sys.path.insert(1, './../')
import cf
import unittest

class Testcf(unittest.TestCase):
    def test_tc1(self):
        self.assertEqual(cf.ej1("("),"NO")
    def test_tc2(self):
        self.assertEqual(cf.ej1("((("),"NO")
    def test_tc3(self):
        self.assertEqual(cf.ej1("()()"),"YES")
    def test_tc4(self):
        self.assertEqual(cf.ej1("[ [  ( )  ] ]"),"YES")
    def test_tc5(self):
        self.assertEqual(cf.ej1(")))"),"NO")
    def test_tc6(self):
        self.assertEqual(cf.ej1("[)"),"NO")
    def test_tc7(self):
        self.assertEqual(cf.ej1(")]"),"NO")
    def test_tc8(self):
        self.assertEqual(cf.ej1("() ["),"NO")
    def test_tc8(self):
        self.assertEqual(cf.ej1("[( )"),"NO")
    def test_tc9(self):
        self.assertEqual(cf.ej1("[ (  [)]]"),"NO")
    def test_tc10(self):
        self.assertEqual(cf.ej1("[[[[[[[[[[[()]]]]]]]]]]]"),"YES")

if __name__ == '__main__':
    unittest.main()
