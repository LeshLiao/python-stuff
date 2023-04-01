import unittest
import my_function


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_compare_max_num(self):
        assert my_function.compare_max_num(1, 2) == 2
        assert my_function.compare_max_num(2, 1) == 2
        assert my_function.compare_max_num(1, 1) == 1


if __name__ == '__main__':
    unittest.main()
