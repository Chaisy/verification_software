import unittest

from L1task5.functions import get_file
from L1task5.tests.const import dirr, right_racsh, NOright_racsh

#проверяем наличие в папке выше файлов с расширением .py и отсуствие файла txt
class TestFiles(unittest.TestCase):
    def test_racsh_files(self):
        result = get_file(dirr, right_racsh)

        self.assertEqual(len(result) > 0, True)

    def test_racsh_files(self):
        result = get_file(dirr, NOright_racsh)

        self.assertEqual(len(result) == 0, True)


if __name__ == '__main__':
    unittest.main()