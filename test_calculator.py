import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(2,3), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1,1),0)
        self.assertEqual(subtract(2,3), -1)
        self.assertEqual(subtract(0,0),0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(10, 10), 100)
        self.assertEqual(multiply(12, 12), 144)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(7, 2), 3.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            divide(0,5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,8), 3)
        self.assertEqual(log(2,16),4)
        self.assertEqual(log(2,32), 5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-1, 100)  # invalid base
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        self.assertRaises(TypeError)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument
        with self.assertRaises(ValueError):
            square_root(-1)

        # Test basic function
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()