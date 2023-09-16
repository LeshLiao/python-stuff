import unittest
from typing import List
from typing import Optional
import linked_list_lib as ll


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        my_list = []

        while head:
            my_list.append(head.val)
            head = head.next
        value = len(my_list) // 2  # round down

        for i in range(value):
            backward_index = -(i+1)
            if my_list[i] != my_list[backward_index]:
                return False
        return True


class TestSolution(unittest.TestCase):
    s = Solution()

    # @unittest.skip
    def test_01(self):
        list = ll.list_to_linked_list([1, 2, 2, 1])
        ll.dump_linked_list(list)
        self.assertEqual(self.s.isPalindrome(list), True)

    def test_02(self):
        list = ll.list_to_linked_list([1, 2])
        ll.dump_linked_list(list)
        self.assertEqual(self.s.isPalindrome(list), False)


if __name__ == '__main__':
    unittest.main()
