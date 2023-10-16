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
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left != None:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_01(self):
        arr = [1,2,5,3,4,None,6]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.s.flatten(root)
        result = bt.binary_tree_to_array(root)
        print(result)
        self.assertEqual(result, [1,None,2,None,3,None,4,None,5,None,6])

    def test_02(self):
        arr = []
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.s.flatten(root)
        result = bt.binary_tree_to_array(root)
        print(result)
        self.assertEqual(result, [])

    def test_03(self):
        arr = [0]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.s.flatten(root)
        result = bt.binary_tree_to_array(root)
        print(result)
        self.assertEqual(result, [0])

if __name__ == '__main__':
    unittest.main()
