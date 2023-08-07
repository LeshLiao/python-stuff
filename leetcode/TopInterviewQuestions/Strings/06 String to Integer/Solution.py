import unittest


class Solution:
    def myAtoi(self, s: str) -> int:

        sign = 1
        digit_str = s.strip()

        if len(digit_str) < 1:
            return 0

        if digit_str[0] == '-':
            sign = -1
            digit_str = digit_str[1:]
        elif digit_str[0] == '+':
            sign = 1
            digit_str = digit_str[1:]

        my_str = ""
        for element in digit_str:
            if element.isdigit():
                my_str = my_str + element
            else:
                break

        if my_str.isdigit() == False:
            return 0

        ret = int(my_str) * sign

        if ret > (pow(2, 31)-1):
            return (pow(2, 31)-1)
        if ret < (pow(2, 31) * -1):
            return (pow(2, 31) * -1)
        return ret

# @unittest.skip('Not ready yet')
# @unittest.skip


class TestStringMethods(unittest.TestCase):
    s = Solution()

    def test_01(self):
        self.assertEqual(self.s.myAtoi(""), 0)

    def test_01(self):
        self.assertEqual(self.s.myAtoi("11111111111111"), (pow(2, 31)-1))

    def test_02(self):
        self.assertEqual(self.s.myAtoi("-1111111111111"), (pow(2, 31) * -1))

    def test_03(self):
        self.assertEqual(self.s.myAtoi("32"), 32)

    def test_04(self):
        self.assertEqual(self.s.myAtoi("-32"), -32)

    def test_example_01(self):
        self.assertEqual(self.s.myAtoi("-32"), -32)

    def test_example_02(self):
        self.assertEqual(self.s.myAtoi("-32"), -32)

    def test_example_03(self):
        self.assertEqual(self.s.myAtoi("-32"), -32)

    def test_submit_01(self):
        self.assertEqual(self.s.myAtoi("words and 987"), 0)

    def test_submit_02(self):
        self.assertEqual(self.s.myAtoi(".1"), 0)

    def test_submit_03(self):
        self.assertEqual(self.s.myAtoi("+-1"), 0)

    def test_submit_04(self):
        self.assertEqual(self.s.myAtoi("4193 with words"), 4193)

    def test_submit_05(self):
        self.assertEqual(self.s.myAtoi("   -42"), -42)


if __name__ == '__main__':
    unittest.main()


''' What did we learn

1. write all the test case (TDD)

2. you need to assume current system only support 32 bit.

3. Dont add unnecessary testcase

'''
