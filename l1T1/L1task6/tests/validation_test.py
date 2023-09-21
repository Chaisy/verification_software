import unittest
from unittest.mock import patch

from L1task6.functions import check_url, check_dir


class TestValidation(unittest.TestCase):
    @patch('builtins.exit')
    def test_url1(self, mock_exit):
        # не пройдет - не полный юрл
        check_url('http://')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_url2(self, mock_exit):
        # не пройдет - нет такого юрл
        check_url('url')
        mock_exit.assert_called_with(-1)

    @patch('builtins.exit')
    def test_directory(self, mock_exit):
        #не пройдет - нет такого
        check_dir('directory')
        mock_exit.assert_called_with(-1)


if __name__ == '__main__':
    unittest.main()