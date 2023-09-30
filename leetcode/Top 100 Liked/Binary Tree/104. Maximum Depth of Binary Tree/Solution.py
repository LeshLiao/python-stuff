import os
import sys
import unittest
from typing import Optional
from typing import List
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import binary_tree_module as bt


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Solution:
    max_val = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        self.printNode(root,0)
        print("max="+str(self.max_val))
        return self.max_val

    def printNode(self,root,current):
        if root:
            current = current + 1
            if current > self.max_val:
                self.max_val = current
            self.printNode(root.left,current)
            print(root.value)
            self.printNode(root.right,current)

class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        arr = [3,9,20,None,None,15,7]
        root = bt.create_binary_tree(arr,0)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.maxDepth(root), 3)

    def test_02(self):
        arr = [1,None,2]
        root = bt.create_binary_tree(arr,0)
        bt.print_binary_tree(root)
        self.assertEqual(self.s.maxDepth(root), 2)



if __name__ == '__main__':
    unittest.main()
