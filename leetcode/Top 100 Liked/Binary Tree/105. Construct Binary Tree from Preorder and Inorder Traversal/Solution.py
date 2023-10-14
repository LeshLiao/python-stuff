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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        if inorder:
            root = TreeNode(preorder[0])
            root_index = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:root_index+1],inorder[:root_index])
            root.right = self.buildTree(preorder[1+root_index:], inorder[root_index+1:])
            return root

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_01(self):
        result = self.s.buildTree([3,9,20,15,7],[9,3,15,20,7])
        bt.print_binary_tree(result)
        # self.assertEqual(bt.bfsTraversalToArray(result), [3,9,20,None,None,15,7])
        self.assertEqual(bt.bfsTraversalToArray(result), [3,9,20,15,7])

    def test_02(self):
        result = self.s.buildTree([-1],[-1])
        bt.print_binary_tree(result)
        self.assertEqual(bt.bfsTraversalToArray(result), [-1])

    def test_03(self):
        result = self.s.buildTree([1,2],[2,1])
        bt.print_binary_tree(result)
        self.assertEqual(bt.bfsTraversalToArray(result), [1,2])

if __name__ == '__main__':
    unittest.main()
