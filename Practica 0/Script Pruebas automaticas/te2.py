import sys
sys.path.insert(1, './../')
import cf
import unittest

class TestHello(unittest.TestCase):
    def test_tc1(self):
        self.assertEqual(cf.ej2("amar amando"),"YES")
    def test_tc2(self):
        self.assertEqual(cf.ej2("llover lloviendo"),"YES")
    def test_tc3(self):
        self.assertEqual(cf.ej2("reir riendo"),"YES")
    def test_tc4(self):
        self.assertEqual(cf.ej2("abatir abatiendo"),"YES")
    def test_tc5(self):
        self.assertEqual(cf.ej2("caer caindo"),"NO")
    def test_tc6(self):
        self.assertEqual(cf.ej2("correr correndo"),"NO")
    def test_tc7(self):
        self.assertEqual(cf.ej2("salir salendo"),"NO")

if __name__ == '__main__':
    unittest.main()
