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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.change_side(root)

    def change_side(self, root):
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.change_side(root.left)
            self.change_side(root.right)
            return root
        return None


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        arr = [4,2,7,1,3,6,9]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        result = self.s.invertTree(root)
        bt.print_binary_tree(result)
        new_arr = bt.binary_tree_to_array(result)
        self.assertEqual(new_arr, [4,7,2,9,6,3,1])

    def test_02(self):
        arr = [2,1,3]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        result = self.s.invertTree(root)
        bt.print_binary_tree(result)
        new_arr = bt.binary_tree_to_array(result)
        self.assertEqual(new_arr, [2,3,1])


if __name__ == '__main__':
    unittest.main()
