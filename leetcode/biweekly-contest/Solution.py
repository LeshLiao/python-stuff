import os
import sys
import unittest
from typing import List
from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # Create a list of dictionaries to keep track of picks for each player
        vec = [defaultdict(int) for _ in range(n)]
        # Populate the list with the pick data
        for p in pick:
            vec[p[0]][p[1]] += 1
        x = 0 # Initialize the count of winning players
        # Iterate through each player
        for i in range(n):
            # Check each picked number for the current player
            print(vec[i].items())
            for k, v in vec[i].items():
                print("k="+str(k))
                print("v="+str(v))
                # If the count of picks for a number is greater than the player's index, they are a winning player
                if v > i:
                    x += 1 # Increment the count of winning players
                    break # Exit the loop as we found the player is winning
        return x # Return the total count of winning players


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):

        self.assertEqual(self.s.winningPlayerCount(2, [[0,8],[0,3]]), 1)

    # def test_ex_2(self):
    #     nums = [3,2,4]
    #     target = 6
    #     self.assertEqual(self.s.twoSum(nums, target), [1, 2])

    # def test_ex_3(self):
    #     nums = [3,3]
    #     target = 6
    #     self.assertEqual(self.s.twoSum(nums, target), [0, 1])

if __name__ == '__main__':
    unittest.main()