import os
import sys
import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return[seen[target - num], i]
            elif num not in seen:
                seen[num] = i

        return []

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        nums = [2,7,11,15]
        target = 9
        self.assertEqual(self.s.twoSum(nums, target), [0, 1])

    def test_ex_2(self):
        nums = [3,2,4]
        target = 6
        self.assertEqual(self.s.twoSum(nums, target), [1, 2])

    def test_ex_3(self):
        nums = [3,3]
        target = 6
        self.assertEqual(self.s.twoSum(nums, target), [0, 1])

if __name__ == '__main__':
    unittest.main()