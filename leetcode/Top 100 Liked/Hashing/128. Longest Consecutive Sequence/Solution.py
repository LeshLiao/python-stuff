import os
import sys
import unittest
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)

        longest_consecutive = 1
        count = 1
        length = len(sorted_list)

        if length < 2:
            return length

        pre = sorted_list[0]
        for i in range(1, length):
            if sorted_list[i] - pre == 1:
                count += 1
                if count > longest_consecutive:
                    longest_consecutive = count
            elif sorted_list[i] == pre:
                pass
            else:
                count = 1
            pre = sorted_list[i]

        return longest_consecutive

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