import ../ej3
import unittest
import sys
from StringIO import StringIO
import subprocess

class TestHello(unittest.TestCase):
    def tc1(self):
        inp = '''
        16
        U=120V and I=5.36A. What is the reason for calculating p? I cant understand ?
        There was a p who has P=560W Which was destroyed by U=291.89V.
        No chance if P=111.11W and I=3.004A.
        U=200VI=4.5A.
        U=220VP=100.00W.
        P=2.5MWI=2A.
        bla bla bla lightning strike I=2A bla bla bla P=2.5MW bla bla voltage?
        If the voltage is U=200V and the current is I=4.5A, which power is generated?
        A light-bulb yields P=100W and the voltage is U=220V. Compute the current, please.
        gU=200VI=4.5A.
        gU=220VP=100.00W.
        tP=2.5MWI=2A.
        PU=200VUI=4.5A.5W
        A light-bulb yields P=0W and the voltage is U=220V. Compute the current, please.
        I light-bulb yields P=1W and the voltage is U=2V. Compute the current, please.
        A light-bulb yields I=-1A and the voltage is U=-2V. Compute the current, please.
        '''
        oup = '''
        Problem #1
        P=643.20W

        Problem #2
        I=1.92A

        Problem #3
        U=36.99V

        Problem #4
        P=900.00W

        Problem #5
        I=0.45A

        Problem #6
        U=1250000.00V

        Problem #7
        U=1250000.00V

        Problem #8
        P=900.00W

        Problem #9
        I=0.45A

        Problem #10
        P=900.00W

        Problem #11
        I=0.45A

        Problem #12
        U=1250000.00V

        Problem #13
        P=900.00W

        Problem #14
        I=0.00A

        Problem #15
        I=0.50A

        Problem #16
        P=2.00W
        '''
        self.assertEqual(ej3.fun(inp),oup)

if __name__ == '__main__':
    unittest.main()
