import unittest

from L1task1.functions import getText
from L1task1.tests.const import right_text, a,b


class TestGetText(unittest.TestCase):
    def test_text(self):
        #функция вернет true при совпадении с префиксом(right_text)
        result = getText().startswith(right_text)

        self.assertEqual(result, True)

    def lenght(self):
        #вычисляем длину получаемой строки, длина нужной и минимальное число 5 <= длина нужной <=длина и максимальное 50
        result = len(right_text) + a <= len(getText()) <= len(right_text) + b

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()