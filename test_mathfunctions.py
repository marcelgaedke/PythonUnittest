#to run unittest:
#Option 1) command line: python -m unittest test_mathfunctions.py
#Option 2) call unittest.main(), this option can run from IDE



print("test_mathfunctions.py")

import unittest
import mathfunctions



print(__name__)


class test_mathfunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mathfunctions.add(10, 5), 15, "10+5 should equal 15")
        self.assertEqual(mathfunctions.add(-10, 10), 0, "-10+10 should equal 0")
        self.assertEqual(mathfunctions.add(-10, -10), -20, "-10+(-10) should equal -20")

    def test_subtract(self):
        self.assertEqual(mathfunctions.subtract(10, 5), 5, "10-5 should equal 5")
        self.assertEqual(mathfunctions.subtract(-10, 10), -20, "-10-10 should equal -20")
        self.assertEqual(mathfunctions.subtract(-10, -10), 0, "-10-(-10) should equal 0")

    def test_multiply(self):
        self.assertEqual(mathfunctions.multiply(10, 5), 50, "10*5 should equal 50")
        self.assertEqual(mathfunctions.multiply(-10, 10), -100, "-10*10 should equal -100")
        self.assertEqual(mathfunctions.multiply(-10, -10), 100, "-10*(-10) should equal 100")

    def test_divide(self):
        self.assertEqual(mathfunctions.divide(10, 5), 2, "10/5 should equal 2")
        self.assertEqual(mathfunctions.divide(-10, 10), -1, "-10/10 should equal -1")
        self.assertEqual(mathfunctions.divide(-10, -10), 1, "-10/(-10) should equal 1")
        self.assertEqual(mathfunctions.divide(10, 4), 2.5, "10/4 should equal 2.5")
        self.assertRaises(ZeroDivisionError, mathfunctions.divide, 10,0)



print("End test_mathfunctions.py")

if __name__ == "__main__":
    unittest.main()


