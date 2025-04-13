from typing import Optional, List
from abc import ABC, abstractmethod

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionInterface(ABC):
    @abstractmethod
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

class Solution(SolutionInterface):
    '''
           Head
             1     ->    2      ->   3  ->   4  ->  5
    prev  current
                     next_node

    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

# --- 🔧 Helper functions ---
def list_to_linkedlist(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

test_cases = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], []),
]

solutions = [Solution()]

for sol in solutions:
    print(f"\nTesting: {sol.__class__.__name__}")
    for i, (p1, expected) in enumerate(test_cases, 1):
        input_linked_list = list_to_linkedlist(p1)
        result_node = sol.reverseList(input_linked_list)
        result_list = linkedlist_to_list(result_node)
        if result_list == expected:
            print(f"  ({i}) passed")
        else:
            print(f"  ({i}) failed. Got {result_list}, expected {expected}")