
import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        print("\nExecunting setUp()...")
        self.__my_calculator = Calculator()

    """SECTION OF TESTS ABOUT func_sum()"""
    def test_sum_return(self):
        """Testing return sum for two numbers"""
        self.assertEqual(self.__my_calculator.func_sum(3, 3), 6)
        self.assertEqual(self.__my_calculator.func_sum(0, 6), 6)
        self.assertEqual(self.__my_calculator.func_sum(-1, 7), 6)

    def test_sum_params(self):
        """Testing return with incorrect parameters"""
        self.assertEqual(self.__my_calculator.func_sum('ss', 1), None)
        self.assertEqual(self.__my_calculator.func_sum(None, 1), None)
        self.assertEqual(self.__my_calculator.func_sum(False, 1), None)

    """SECTION OF TESTS ABOUT func_sub()"""
    def test_sub_return(self):
        """Testing return sub for two numbers"""
        self.assertEqual(self.__my_calculator.func_sub(3, 3), 0)
        self.assertEqual(self.__my_calculator.func_sub(0, 6), -6)
        self.assertEqual(self.__my_calculator.func_sub(-1, 7), -8)

    def test_sub_params(self):
        """Testing return with incorrect parameters"""
        self.assertEqual(self.__my_calculator.func_sub('ss', 1), None)
        self.assertEqual(self.__my_calculator.func_sub(None, 1), None)
        self.assertEqual(self.__my_calculator.func_sub(False, 1), None)

    """SECTION OF TESTS ABOUT func_mul()"""
    def test_mul_return(self):
        """Testing return mul for two numbers"""
        self.assertEqual(self.__my_calculator.func_mul(3, 3), 9)
        self.assertEqual(self.__my_calculator.func_mul(0, 6), 0)
        self.assertEqual(self.__my_calculator.func_mul(-1, 7), -7)

    def test_mul_params(self):
        """Testing return with incorrect parameters"""
        self.assertEqual(self.__my_calculator.func_mul('ss', 1), None)
        self.assertEqual(self.__my_calculator.func_mul(None, 1), None)
        self.assertEqual(self.__my_calculator.func_mul(False, 1), None)

    """SECTION OF TESTS ABOUT func_div()"""
    def test_div_return(self):
        """Testing return div for two numbers"""
        self.assertEqual(self.__my_calculator.func_div(3, 3), 1)
        self.assertEqual(self.__my_calculator.func_div(0, 6), 0)
        self.assertEqual(self.__my_calculator.func_div(-1, 7), -0.14285714285714285)

    def test_div_params(self):
        """Testing return with incorrect parameters"""
        self.assertEqual(self.__my_calculator.func_div('ss', 1), None)
        self.assertEqual(self.__my_calculator.func_div(None, 1), None)
        self.assertEqual(self.__my_calculator.func_div(False, 1), None)


    def tearDown(self):
        print("\nExecunting tearDown()...")
        pass


if __name__ == '__main__':
    unittest.main()
