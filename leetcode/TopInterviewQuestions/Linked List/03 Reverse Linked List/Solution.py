import unittest
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        head = self.list_to_linked_list([2, 4, 6, 8, 10])
        reversed = self.s.reverseList(head)
        # self.dump_linked_list(reversed)
        self.assertEqual(self.linked_list_to_list(reversed), [10, 8, 6, 4, 2])

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

    def dump_linked_list(self, head: ListNode):
        cur = head
        while cur != None:
            print("cur.val=" + str(cur.val))
            cur = cur.next


if __name__ == '__main__':
    unittest.main()
