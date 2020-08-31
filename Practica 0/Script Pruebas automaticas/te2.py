import ../ej2
import unittest
import sys
from StringIO import StringIO
import subprocess

class TestHello(unittest.TestCase):
    def tc1(self):
        self.assertEqual(ej2.fun("amar amando"),"YES")
    def tc2(self):
        self.assertEqual(ej2.fun("llover lloviendo"),"YES")
    def tc3(self):
        self.assertEqual(ej2.fun("reir riendo"),"YES")
    def tc4(self):
        self.assertEqual(ej2.fun("abatir abatiendo"),"YES")
    def tc5(self):
        self.assertEqual(ej2.fun("caer caindo"),"NO")
    def tc6(self):
        self.assertEqual(ej2.fun("correr correndo"),"NO")
    def tc7(self):
        self.assertEqual(ej2.fun("salir salendo"),"NO")

if __name__ == '__main__':
    unittest.main()
