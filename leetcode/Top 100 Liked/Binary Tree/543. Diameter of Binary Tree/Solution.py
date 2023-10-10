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
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.cal_depth(root)
        return self.diameter

    def cal_depth(self, root):
        if root:
            left_depth = self.cal_depth(root.left)
            right_depth = self.cal_depth(root.right)
            if left_depth + right_depth > self.diameter:
                self.diameter = left_depth + right_depth
            return 1 + max(left_depth, right_depth)
        else:
            return 0 

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    # @unittest.skip
    def test_01(self):
        arr = [1,2,3,4,5]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.diameterOfBinaryTree(root)
        self.assertEqual(result, 3)

    def test_02(self):
        arr = [1,2]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.diameterOfBinaryTree(root)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
