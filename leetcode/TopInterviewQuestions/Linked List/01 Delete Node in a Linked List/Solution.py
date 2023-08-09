import unittest
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


class TestSolution(unittest.TestCase):
    s = Solution()

    def test_01(self):
        head = ListNode(4)

        first_node = ListNode(5)
        head.next = first_node

        second_node = ListNode(1)
        first_node.next = second_node

        third_node = ListNode(9)
        second_node.next = third_node

        test_node = ListNode(5)

        self.turn_to_list(head)
        self.s.deleteNode(first_node)
        self.assertEqual(self.turn_to_list(head), [4, 1, 9])

    def turn_to_list(self, head: ListNode) -> List:
        node = head
        my_list = []
        while (node != None):
            my_list.append(node.val)
            node = node.next
        print(my_list)
        return my_list


if __name__ == '__main__':
    unittest.main()
