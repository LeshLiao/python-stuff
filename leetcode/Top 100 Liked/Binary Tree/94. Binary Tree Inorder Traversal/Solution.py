import unittest
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
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
            self.my_list.append(root.val)
            self.in_order(root.right)


def insert(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if root.val > val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root


def printNode(root):
    if root:
        printNode(root.left)
        print(root.val)
        printNode(root.right)


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):

        r = TreeNode(5)
        r = insert(r, 9)
        r = insert(r, 6)

        printNode(r)
        self.assertEqual(self.s.inorderTraversal(r), [5, 6, 9])


'''
    5
        9
      6
'''

if __name__ == '__main__':
    unittest.main()
