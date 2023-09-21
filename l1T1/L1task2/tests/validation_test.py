import unittest
from unittest.mock import patch

from L1task2.functions import check, check_age


class TestValidation(unittest.TestCase):
    @patch('builtins.exit')
    def test_check_validation1(self, mock_exit):
        #не пройдет - маленткая буква
        check('ann')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_check_validation2(self, mock_exit):
        # не пройдет - недопустимые знаки
        check('!ттоо/')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_check_validation3(self, mock_exit):
        # не пройдет - цифры
        check('8')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_check_validation4(self, mock_exit):
        # не пройдет - не слово одно
        check('anna dfghj')
        mock_exit.assert_called_with(-1)
#проверка возраста
    @patch('builtins.exit')
    def test_age_validation1(self, mock_exit):
        # не пройдет - бувы
        check_age('dfghk')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_age_validation2(self, mock_exit):
        # не пройдет - вышло за ограничение 100
        check('123456780')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_age_validation3(self, mock_exit):
        # не пройдет - не одно число
        check('123 456 780')
        mock_exit.assert_called_with(-1)


if __name__ == '__main__':
    unittest.main()