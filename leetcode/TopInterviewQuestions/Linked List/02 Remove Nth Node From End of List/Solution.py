import unittest
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        node = head
        '''
        my_list = []
        while (node != None):
            my_list.append(node.val)
            node = node.next
        print(my_list)
        '''
        if head.next == None and n == 1:
            head = None
            return head

        for element in range(n):
            slow = slow.next

        if slow == None:
            print("None!!")
            head.val = head.next.val
            head.next = head.next.next
            # print("head.val="+str(head.val))
            return head

        while (slow.next != None):
            fast = fast.next
            slow = slow.next

        print("fast.val="+str(fast.next.val))

        if n == 1:
            fast.next = None
        else:
            self.deleteNode(fast.next)
        return head


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
        self.s.removeNthFromEnd(head, 1)
        self.assertEqual(self.turn_to_list(head), [4, 5, 1])

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
