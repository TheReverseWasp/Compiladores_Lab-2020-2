import ../ej1
import unittest
import sys
from StringIO import StringIO
import subprocess

class TestHello(unittest.TestCase):
    def tc1(self):
        self.assertEqual(ej1.fun("("),"NO")
    def tc2(self):
        self.assertEqual(ej1.fun("((("),"NO")
    def tc3(self):
        self.assertEqual(ej1.fun("()()"),"YES")
    def tc4(self):
        self.assertEqual(ej1.fun("[ [  ( )  ] ]"),"YES")
    def tc5(self):
        self.assertEqual(ej1.fun(")))"),"NO")
    def tc6(self):
        self.assertEqual(ej1.fun("[)"),"NO")
    def tc7(self):
        self.assertEqual(ej1.fun(")]"),"NO")
    def tc8(self):
        self.assertEqual(ej1.fun("() ["),"NO")
    def tc8(self):
        self.assertEqual(ej1.fun("[( )"),"NO")
    def tc9(self):
        self.assertEqual(ej1.fun("[ (  [)]]"),"NO")
    def tc10(self):
        self.assertEqual(ej1.fun("[[[[[[[[[[[()]]]]]]]]]]]"),"YES")

if __name__ == '__main__':
    unittest.main()
