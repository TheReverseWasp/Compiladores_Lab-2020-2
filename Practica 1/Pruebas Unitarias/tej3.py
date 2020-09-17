import sys
sys.path.insert(1, './../Ejercicios/regex')
from funs import *
import unittest

class Testcf(unittest.TestCase):
    def test_tc1(self):
        self.assertEqual(ej3("me gustaria pedirle un racimo de platanos, desearia encargarle un PSP. Quisiera pedirle odio."), "SOLICITUDES: ['un racimo de platanos', 'un PSP', 'odio']")
    def test_tc2(self):
        self.assertEqual(ej3("avsfasjnianfi"), "NO HAY UNA SOLICITUD")
if __name__ == '__main__':
    unittest.main()
