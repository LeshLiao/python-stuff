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
        self.current_level = 0
        self.sub_list = []
        self.all_list = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.catch_by_level(root, 0)

    def catch_by_level(self, root, level_num):
        if root == None:
            return []

        queue = [[root,level_num]]
        while queue:
            list = queue.pop(0)
            node = list[0]
            level_num = list[1]
            if node:
                print(str(node.val)+ ",")
                if self.current_level == level_num:
                    if node.val != None:
                        self.sub_list.append(node.val)
                else:
                    self.all_list.append(self.sub_list)
                    self.sub_list = []
                    self.current_level = self.current_level + 1
                    if node.val != None:
                        self.sub_list.append(node.val)

                queue.append([node.left, level_num + 1])
                queue.append([node.right, level_num + 1])
        self.all_list.append(self.sub_list)

        print(self.all_list)
        return self.all_list


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