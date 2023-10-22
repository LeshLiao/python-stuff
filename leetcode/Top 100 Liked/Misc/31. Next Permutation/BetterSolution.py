import unittest
from typing import List

class Solution:
    '''
        Refer to: Oloy, Link:https://leetcode.com/problems/next-permutation/discuss/1909728/Simple-9-line-Python-Solution-with-Detailed-Explanation-(Easy-Understand-for-Beginners!)
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, 0, -1):
            # find the index of the last peak
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                # get the index before the last peak
                j = i - 1
                # swap the pre-last peak index with the value just large than it
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return
        nums.reverse()
        return

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_ex1(self):
        nums = [1,2,3]
        excepted = [1,3,2]
        self.s.nextPermutation(nums)
        self.assertEqual(nums, excepted)

    def test_ex2(self):
        nums = [3,2,1]
        excepted = [1,2,3]
        self.s.nextPermutation(nums)
        self.assertEqual(nums, excepted)

    def test_ex3(self):
        nums = [1,1,5]
        excepted = [1,5,1]
        self.s.nextPermutation(nums)
        self.assertEqual(nums, excepted)

    def test_submit_1(self):
        nums = [2,3,1]
        excepted = [3,1,2]
        self.s.nextPermutation(nums)
        self.assertEqual(nums, excepted)

    def test_submit_1(self):
        nums = [1,3,2]
        excepted = [2,1,3]
        self.s.nextPermutation(nums)
        self.assertEqual(nums, excepted)

    def test_private_1(self):
        nums = [1,2,4,3]
        excepted = [1,3,2,4]
        self.s.nextPermutation(nums)
        self.assertEqual(nums, excepted)

if __name__ == '__main__':
    unittest.main()