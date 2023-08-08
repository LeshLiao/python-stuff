from typing import List
import unittest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        long_prefix = ""
        max_length = 0
        max_str = ""

        # looking for max length string
        for my_str in strs:
            if len(my_str) > max_length:
                max_length = len(my_str)
                max_str = my_str
        # print("max_str:"+max_str)
        # print("max_length:"+str(max_length))

        # iterate and check every character by max string
        for i in range(len(max_str)):
            for my_str in strs:
                if i >= len(my_str):
                    return long_prefix
                if my_str[i] != max_str[i]:
                    return long_prefix
            long_prefix = long_prefix + max_str[i]

        return long_prefix


class TestSolution(unittest.TestCase):
    s = Solution()

    def test_01(self):
        self.assertEqual(self.s.longestCommonPrefix(
            ["flower", "flow", "flight"]), "fl")

    def test_02(self):
        self.assertEqual(self.s.longestCommonPrefix(
            ["dog", "racecar", "car"]), "")

    def test_submit_01(self):
        self.assertEqual(self.s.longestCommonPrefix(
            ["", "b"]), "")

    def test_submit_02(self):
        self.assertEqual(self.s.longestCommonPrefix(
            ["ab", "a"]), "a")


if __name__ == '__main__':
    unittest.main()


''' What did we learn
You should add more self testcase to test empty string case.
'''
