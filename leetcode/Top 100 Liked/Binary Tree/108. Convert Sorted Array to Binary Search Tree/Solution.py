import unittest
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, data):
        if data < self.val:
            if self.left == None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    # function to print a BST
    def PrintTree(self):
        print(self.val)

        if self.left:
            self.left.PrintTree()

        if self.right:
            self.right.PrintTree()


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        my_list = [1, 2, 3]
        root = TreeNode(0)
        for data in my_list:
            self.addToTree(root, data)


class TestSolution(unittest.TestCase):
    s = Solution()

    @unittest.skip
    def test_01(self):
        list = ll.list_to_linked_list([1, 2, 2, 1])
        self.assertEqual(self.s.isPalindrome(list), True)

    def test_private(self):

        # Use the insert method to add nodes
        root = TreeNode(12)
        root.insert(6)
        root.insert(14)
        root.insert(3)

        root.PrintTree()
        self.assertEqual(True, True)


'''
        12
    6       14
3

12 6 14 3
'''


if __name__ == '__main__':
    unittest.main()
