import unittest
from unittest.mock import patch

from L1task5.functions import check_dir, check_racsh

#проверяем сущесвование
class TestValidation(unittest.TestCase):
    @patch('builtins.exit')
    def test_directory(self, mock_exit):

        check_dir('dirrr')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_extension(self, mock_exit):
        check_racsh('racsh')
        mock_exit.assert_called_with(-1)


if __name__ == '__main__':
    unittest.main()