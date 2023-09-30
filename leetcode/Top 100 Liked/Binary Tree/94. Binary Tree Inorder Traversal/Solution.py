import unittest
from typing import List
from typing import Optional
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import binary_tree_module as bt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


class Solution:
    my_list = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.my_list = []
        self.in_order(root)
        return self.my_list

    def in_order(self, root) -> List[int]:
        if root:
            self.in_order(root.left)
            if root.value:
                self.my_list.append(root.value)
            self.in_order(root.right)


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        arr = [1,None,2,None,None,3]
        root = bt.create_binary_tree(arr,0)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.inorderTraversal(root), [1, 3, 2])

if __name__ == '__main__':
    unittest.main()
