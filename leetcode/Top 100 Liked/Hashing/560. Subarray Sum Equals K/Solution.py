import unittest
from typing import List

class Solution:
    '''
        refer to : https://www.youtube.com/watch?v=EFzYA9H0MfQ
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:

        temp = {}
        count = 0
        sum = 0

        for num in nums:
            sum += num
            if sum == k:
                count += 1
            if sum - k in temp:
                count += temp[sum - k]

            if sum in temp:
                temp[sum] += 1
            else:
                temp[sum] = 1

        return count

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        nums = [1,1,1]
        k = 2
        expected = 2
        self.assertEqual(self.s.subarraySum(nums, k), expected)

    def test_ex_2(self):
        nums = [1,2,3]
        k = 3
        expected = 2
        self.assertEqual(self.s.subarraySum(nums, k), expected)

if __name__ == '__main__':
    unittest.main()