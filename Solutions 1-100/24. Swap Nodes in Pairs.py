from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        startNode = ListNode(0, head)
        current = head
        previous = startNode

        while current and current.next:
            next_pair_start = current.next.next
            previous.next = current.next
            temp = current.next.next
            current.next.next = current
            current.next = next_pair_start
            previous = current
            current = current.next

        return startNode.next
