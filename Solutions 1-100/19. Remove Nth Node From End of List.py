from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        ptr = head
        length = 0

        while ptr:
            length += 1
            ptr = ptr.next

        target = length - n
        if target == 0:
            return head.next

        ptr = head
        for _ in range(target - 1):
            ptr = ptr.next

        ptr.next = ptr.next.next if ptr.next else None

        return head
