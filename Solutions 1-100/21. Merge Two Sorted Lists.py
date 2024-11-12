from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        ptr = ListNode()
        ptr.next = None
        head = ptr

        while list1 or list2:
            newNode = ListNode()
            if not list1:
                newNode.val = list2.val
                newNode.next = list2.next
                list2 = list2.next
            elif not list2:
                newNode.val = list1.val
                newNode.next = list1.next
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    newNode.val = list1.val
                    newNode.next = list1.next
                    list1 = list1.next
                else:
                    newNode.val = list2.val
                    newNode.next = list2.next
                    list2 = list2.next
            ptr.next = newNode
            ptr = ptr.next

        return head.next
