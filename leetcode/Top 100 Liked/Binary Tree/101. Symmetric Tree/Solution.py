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
        pass

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root and root.left == None and root.right == None:
            return True

        if root == None or root.left == None or root.right == None:
            return False

        return self.identicalTrees(root.left, self.revert_bst(root.right))

    def revert_bst(self,root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.revert_bst(root.left)
            self.revert_bst(root.right)
            return root
        return None

    def identicalTrees(self, a, b):

        # 1. Both empty
        if a is None and b is None:
            return True

        # 2. Both non-empty -> Compare them
        if a is not None and b is not None:
            if a.val != b.val:
                return False
            return self.identicalTrees(a.left, b.left) and self.identicalTrees(a.right, b.right)

        # 3. one empty, one not -- false
        return False

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_01(self):
        arr = [1,2,2,3,4,4,3]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        result = self.s.isSymmetric(root)
        self.assertEqual(result, True)

    def test_02(self):
        arr = [1,2,2,None,3,None,3]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        result = self.s.isSymmetric(root)
        self.assertEqual(result, False)

    def test_03(self):
        arr = [1,2,2,2,None,2]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        result = self.s.isSymmetric(root)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
