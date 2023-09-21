import unittest

from L1task3.functions import get_square


class TestSquare(unittest.TestCase):
    def test_square(self):
#проверяем правильность подсета площади
        self.assertEqual(get_square(6, 20), 120)

    def test_square1(self):
#проверяем правильность подсета площади
        self.assertEqual(get_square(10, 50), 500)


if __name__ == '__main__':
    unittest.main()