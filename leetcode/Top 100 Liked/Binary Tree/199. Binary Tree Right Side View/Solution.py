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
        self.return_list = []
        self.temp_list = []
        self.max_level = 1

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root, 1)

        for i in range(1,self.max_level+1):
            for item in reversed(self.temp_list):
                if item[1] == i:
                    self.return_list.append(item[0])
                    break

        return self.return_list

    def traversal(self, root, level):
        if root:
            self.temp_list.append([root.val, level])

            if level > self.max_level:
                self.max_level = level

            self.traversal(root.left, level + 1)
            self.traversal(root.right, level + 1)

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_ex_1(self):
        arr = [1,2,3,None,5,None,4]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.rightSideView(root), [1,3,4])

    def test_ex_2(self):
        arr =  [1,None,3]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.rightSideView(root), [1,3])

    def test_ex_3(self):
        arr =  []
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.rightSideView(root), [])

    def test_submit_1(self):
        arr =  [1,2,3,4]
        root = bt.array_to_binary_tree(arr)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.rightSideView(root), [1,3,4])

if __name__ == '__main__':
    unittest.main()
