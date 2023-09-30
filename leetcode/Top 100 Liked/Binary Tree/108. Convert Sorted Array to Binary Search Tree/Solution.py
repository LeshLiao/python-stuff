import os
import sys
import unittest
from typing import Optional
from typing import List
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import binary_tree_module as bt


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.create_balance_tree(nums, 0, len(nums)-1)

    def create_balance_tree(self,arr, left,right):
        if left > right:
            return None
        center = (left + right) // 2
        root = TreeNode(arr[center])
        root.left = self.create_balance_tree(arr,left,center -1)
        root.right = self.create_balance_tree(arr,center + 1,right)
        return root


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        arr = [-10,-3,0,5,9]
        result = self.s.sortedArrayToBST(arr)
        root = bt.print_binary_tree(result)
        new_arr = bt.bfsTraversalToArray(result)
        # self.assertEqual(new_arr, [0,-10,5,None,-3,None,9])
        self.assertEqual(new_arr, [0,-10,5,-3,9])

'''
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
'''


if __name__ == '__main__':
    unittest.main()
