import unittest
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        nums_len = len(nums)
        for i in range(nums_len-1, 0, -1):
            if nums[i] > nums[i-1]:
                if i == nums_len-1:
                    self.swap_num(nums, i, i-1)
                    break
                else:
                    for j in range(nums_len-1, i-1, -1):
                        if nums[j] > nums[i-1]:
                            self.swap_num(nums, i-1, j)
                            break
                    self.sort_sub_array(nums, i, nums_len)
                    break
            if i == 1:
                self.sort_sub_array(nums, 0, nums_len)

    def swap_num(self,nums, x, y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp

    def sort_sub_array(self,nums, begin, end):
        sub_list = sorted(nums[begin:end])
        for i in range(begin,end):
            nums[i] = sub_list[i-begin]

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