from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ret = ListNode(0, head)
        prev = ret
        cur = head

        while cur:
            start = cur

            test = cur
            for i in range(k):
                if not test:
                    return ret.next
                test = test.next

            last = None
            for i in range(k):
                nxt = cur.next
                cur.next = last
                last = cur
                cur = nxt

            prev.next = last
            start.next = cur
            prev = start

        return ret.next