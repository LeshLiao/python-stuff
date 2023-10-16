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
        self.target = 0
        self.num = 0
        self.my_list = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.target = k
        self.num = 0
        self.help(root)
        return self.my_list[k-1]

    def help(self, root):
        if root:
            self.help(root.left)
            self.my_list.append(root.val)
            self.help(root.right)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        arr = [3,1,4,None,2]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.kthSmallest(root, 1), 1)

    def test_ex_2(self):
        arr =  [5,3,6,2,4,None,None,1]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.kthSmallest(root, 3), 3)

if __name__ == '__main__':
    unittest.main()