import unittest
from unittest.mock import patch

from L1task3.functions import check_hw


class TestValidation(unittest.TestCase):
    @patch('builtins.exit')
    def test_hw_validation1(self, mock_exit):
        #не пройдет - отрицательное
        check_hw('-8')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_hw_validation2(self, mock_exit):
        # не пройдет - буквы
        check_hw('sdfghjk')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_hw_validation3(self, mock_exit):
        # не пройдет - 0
        check_hw('0')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_hw_validation4(self, mock_exit):
        # не пройдет - мусор среди цифр
        check_hw('6-9')
        mock_exit.assert_called_with(-1)


if __name__ == '__main__':
    unittest.main()