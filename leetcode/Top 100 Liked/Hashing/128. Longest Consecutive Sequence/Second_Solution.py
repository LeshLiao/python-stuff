import os
import sys
import unittest
from typing import List

class Solution:
    '''
    refer to "StefanPochmann"
    '''
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        nums = [100,4,200,1,3,2]
        expected = 4
        self.assertEqual(self.s.longestConsecutive(nums), expected)

    def test_ex_2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        expected = 9
        self.assertEqual(self.s.longestConsecutive(nums), expected)

if __name__ == '__main__':
    unittest.main()