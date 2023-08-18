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

    @unittest.skip
    def test_something(self):
        list = [111, 2, 3]
        head = self.list_to_linked_list(list)
        self.turn_to_list(head)

    # @unittest.skip
    def test_01(self):
        head = self.list_to_linked_list([4, 5, 1, 9])
        self.s.removeNthFromEnd(head, 1)
        self.assertEqual(self.linked_list_to_list(head), [4, 5, 1])

    def linked_list_to_list(self, head: ListNode) -> List:
        cur = head
        my_list = []
        while (cur != None):
            my_list.append(cur.val)
            cur = cur.next
        print(my_list)
        return my_list

    def list_to_linked_list(self, list: List) -> ListNode:
        if len(list) == 0:
            return None
        head = ListNode(list[0])
        cur = head
        for item in list[1:]:
            cur.next = ListNode(item)
            cur = cur.next
        return head


if __name__ == '__main__':
    unittest.main()
