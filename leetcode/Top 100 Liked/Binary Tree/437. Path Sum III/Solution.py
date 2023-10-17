import os
import sys
import unittest
from typing import Optional
from typing import List
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import binary_tree_module as bt

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.dfs(root, targetSum)
        return self.count

    def dfs(self,root, targetSum):
        if root:
            self.test(root, targetSum)
            self.dfs(root.left, targetSum)
            self.dfs(root.right, targetSum)

    def test(self,root, temp):
        if root:
            if root.val == temp:
                self.count += 1
            self.test(root.left, temp - root.val)
            self.test(root.right, temp - root.val)
            return 0

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        arr =  [10,5,-3,3,2,None,11,3,-2,None,1]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        targetSum = 8
        self.assertEqual(self.s.pathSum(root, targetSum), 3)

    def test_ex_2(self):
        arr =  [5,4,8,11,None,13,4,7,2,None,None,5,1]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        targetSum = 22
        self.assertEqual(self.s.pathSum(root, targetSum), 3)

if __name__ == '__main__':
    unittest.main()