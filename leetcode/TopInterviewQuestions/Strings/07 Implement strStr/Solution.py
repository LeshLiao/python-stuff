import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:(i+len(needle))] == needle:
                return i
        return -1


class TestStringMethods(unittest.TestCase):
    s = Solution()

    def test_01(self):
        self.assertEqual(self.s.strStr("sadbutsad", "sad"), 0)

    def test_02(self):
        self.assertEqual(self.s.strStr("leetcode", "leeto"), -1)

    # @unittest.skip
    def test_submit_01(self):
        self.assertEqual(self.s.strStr("abc", "c"), 2)


if __name__ == '__main__':
    unittest.main()


''' What did we learn
check for loop end of index carefully

'''
