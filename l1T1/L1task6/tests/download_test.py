import unittest
from unittest.mock import patch

from L1task6.functions import saving, check_url
from L1task6.tests.const import r_dirr, urls


class TestDownload(unittest.TestCase):
    @patch('builtins.exit')
    def test_russ_file(self, mock_exit):
        #
        url = check_url(urls[0])
        saving(url, r_dirr, False)

        mock_exit.assert_not_called()

    @patch('builtins.exit')
    def test_image_file_with_parameters(self, mock_exit):
        url = check_url(urls[1])
        print(url)
        saving(url, r_dirr, False)

        mock_exit.assert_not_called()

    @patch('builtins.exit')
    def test_image_file(self, mock_exit):
        url = check_url(urls[2])
        saving(url, r_dirr, False)

        mock_exit.assert_not_called()

    @patch('builtins.exit')
    def test_page(self, mock_exit):
        url = check_url(urls[3])
        saving(url, r_dirr, False)

        mock_exit.assert_called_with(-1)


if __name__ == '__main__':
    unittest.main()