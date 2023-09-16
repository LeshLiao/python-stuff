from typing import List
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_list(head: ListNode) -> List:
    cur = head
    my_list = []
    while (cur != None):
        my_list.append(cur.val)
        cur = cur.next
    print(my_list)
    return my_list


def list_to_linked_list(list: List) -> ListNode:
    if len(list) == 0:
        return None
    head = ListNode(list[0])
    cur = head
    for item in list[1:]:
        cur.next = ListNode(item)
        cur = cur.next
    return head


def dump_linked_list(head: ListNode):
    cur = head
    list_val = ""
    while cur != None:
        list_val = list_val + str(cur.val) + ", "
        cur = cur.next
    print(list_val)


if __name__ == '__main__':
    print("run __name__")
