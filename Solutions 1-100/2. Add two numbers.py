from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        b = 0

        c = 0
        while l1:
            a = a + l1.val * (10 ** c)
            c += 1
            l1 = l1.next

        c = 0
        while l2:
            b = b + l2.val * (10 ** c)
            c += 1
            l2 = l2.next

        result = a + b

        new_node = ListNode(result % 10)
        l3 = new_node
        result //= 10
        while result > 0:
            new_node.next = ListNode(result % 10)
            new_node = new_node.next
            new_node.next = None
            result //= 10

        return l3
