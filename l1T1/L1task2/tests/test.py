import unittest

from L1task2.functions import sort_age
from L1task2.tests.const import right_massiv, result_age


class TestAges(unittest.TestCase):
    def test_something(self):
#сравниваем полученные данные о возрасте при функции и вручную введенные
        self.assertTupleEqual(sort_age(right_massiv), result_age)


if __name__ == '__main__':
    unittest.main()