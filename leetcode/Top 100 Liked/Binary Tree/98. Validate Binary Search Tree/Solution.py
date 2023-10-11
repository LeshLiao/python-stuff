import os
import sys
import unittest
from typing import Optional
from typing import List
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import binary_tree_module as bt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.in_order_list = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.in_order(root)
        for i in range(1,len(self.in_order_list)):
            if self.in_order_list[i-1] >= self.in_order_list[i]:
                return False 
        return True
    
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            if root.val != None:
                self.in_order_list.append(root.val)
            self.in_order(root.right)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    # @unittest.skip
    def test_01(self):
        arr = [2,1,3]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.isValidBST(root)
        self.assertEqual(result, True)

    def test_02(self):
        arr = [5,1,4,None,None,3,6]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.isValidBST(root)
        self.assertEqual(result, False)

    def test_03(self):
        arr = [0,None,-1]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.isValidBST(root)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
