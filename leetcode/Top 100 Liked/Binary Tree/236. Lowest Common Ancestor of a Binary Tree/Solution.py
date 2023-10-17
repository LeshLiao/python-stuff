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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root == None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left != None and right != None:
            return root
        if left == None and right == None:
            return None

        if left:
            return left
        else:
            return right

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        arr = [3,5,1,6,2,0,8,None,None,7,4]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        p = 5
        q = 1
        node = self.s.lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
        self.assertEqual(node.val, 3)

    def test_ex_2(self):
        arr = [3,5,1,6,2,0,8,None,None,7,4]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        p = 5
        q = 4
        node = self.s.lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
        self.assertEqual(node.val, 5)

    def test_ex_3(self):
        arr = [1,2]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        p = 1
        q = 2
        node = self.s.lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
        self.assertEqual(node.val, 1)

if __name__ == '__main__':
    unittest.main()