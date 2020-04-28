import unittest
from unittest.mock import Mock
from unittest.mock import patch
from unnecessary_math import multiply
from calculuspaper1 import calculator
from calculuspaper1 import Calculator

class TestCalculator(unittest.TestCase):
    #@patch('main.Calculator.sum', return_value=9)
    def setUp(self):
        self.calc = Calculator()
        #pass

    def test_sum(self):
        answer1 = self.calc.sum(2, 4)
        answer2 = calculator(4,2)
        self.assertEqual(answer1, 6)
        self.assertEqual(answer2, 6)

    def test_sum_mocking(self):
        mock = Mock()
        mock.sum()
        self.calc.sum = mock
        self.calc.sum.return_value = 10
        answer1 = self.calc.sum(2, 4)
        self.calc.sum.assert_called_with(2,4)
        self.calc.sum.assert_called_once()
        #self.calc.assert_
        #self.assertEqual(answer1, 6)


if __name__ == '__main__':
    unittest.main()