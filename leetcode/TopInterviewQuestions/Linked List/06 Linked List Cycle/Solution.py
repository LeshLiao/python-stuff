import unittest
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        head = self.list_to_cycle_linked_list([3, 2, 0, -4], 1)
        # head = self.list_to_cycle_linked_list([3, 2, 0, -4], 0)   # non-cycle if pos = 0
        self.dump_cycle_linked_list(head, 10)
        self.assertEqual(self.s.hasCycle(head), True)

    def list_to_cycle_linked_list(self, list: List, pos: int) -> ListNode:
        if len(list) == 0:
            return None
        head = ListNode(list[0])
        cur = head
        index = 0
        cycle_node = None
        for item in list[1:]:
            index = index + 1
            cur.next = ListNode(item)
            cur = cur.next
            if pos == index:
                cycle_node = cur
        cur.next = cycle_node
        return head

    def dump_cycle_linked_list(self, head: ListNode, max_num: int):
        cur = head
        index = 0
        while cur != None:
            print("cur.val=" + str(cur.val))
            cur = cur.next
            index = index + 1
            if index > max_num:
                break


if __name__ == '__main__':
    unittest.main()
