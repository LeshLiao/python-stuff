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
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_values = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)
                if node.val != None:
                    level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_values)

        return result

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_01(self):
        arr = [3,9,20,None,None,15,7]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.levelOrder(root)
        self.assertEqual(result, [[3],[9,20],[15,7]])

    def test_02(self):
        arr = [1]
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.levelOrder(root)
        self.assertEqual(result, [[1]])

    def test_03(self):
        arr = []
        root = bt.create_binary_tree(arr, 0)
        bt.print_binary_tree(root)
        result = self.s.levelOrder(root)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()