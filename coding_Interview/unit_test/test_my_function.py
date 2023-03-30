import unittest
import my_function

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_compare_max_num(self):
        assert my_function.compare_max_num(1, 2) == 2
        assert my_function.compare_max_num(2, 1) == 2
        assert my_function.compare_max_num(1, 1) == 1
        
if __name__ == '__main__':
    unittest.main()