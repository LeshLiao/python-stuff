import unittest
from typing import List

class Solution:
    '''
        Refer to : NeetCode(https://www.youtube.com/watch?v=5WZl3MMT0Eg&t=317s)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        max_sum = sum
        for i in range(1,len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            max_sum = max(sum, max_sum)
        return max_sum

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_ex1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        excepted = 6
        self.assertEqual(self.s.maxSubArray(nums), excepted)

    def test_ex2(self):
        nums = [1]
        excepted = 1
        self.assertEqual(self.s.maxSubArray(nums), excepted)

    def test_ex3(self):
        nums = [5,4,-1,7,8]
        excepted = 23
        self.assertEqual(self.s.maxSubArray(nums), excepted)

if __name__ == '__main__':
    unittest.main()