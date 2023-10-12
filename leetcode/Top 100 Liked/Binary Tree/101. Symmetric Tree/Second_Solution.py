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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root and root.left == None and root.right == None:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):

        # 1. Both empty
        if left is None and right is None:
            return True

        # 2. Both non-empty -> Compare them
        if left is not None and right is not None:
            if left.val != right.val:
                return False
            return self.isMirror(left.left, right.right) and \
                   self.isMirror(left.right, right.left)

        # 3. one empty, one not -- false
        return False


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_01(self):
        arr = [1,2,2,3,4,4,3]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.isSymmetric(root)
        self.assertEqual(result, True)

    def test_02(self):
        arr = [1,2,2,None,3,None,3]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.isSymmetric(root)
        self.assertEqual(result, False)

    def test_03(self):
        arr = [1,2,2,2,None,2]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.isSymmetric(root)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
