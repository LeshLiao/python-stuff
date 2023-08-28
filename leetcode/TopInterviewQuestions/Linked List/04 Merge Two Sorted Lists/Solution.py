import unittest
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iteratively


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        list1 = self.list_to_linked_list([1, 2, 4])
        list2 = self.list_to_linked_list([1, 3, 4])
        self.dump_linked_list(list1)
        self.dump_linked_list(list2)
        self.assertEqual(self.linked_list_to_list(self.s.mergeTwoLists(
            list1, list2)), [1, 1, 2, 3, 4, 4])

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
        list_val = ""
        while cur != None:
            list_val = list_val + str(cur.val) + ", "
            cur = cur.next
        print(list_val)


if __name__ == '__main__':
    unittest.main()
