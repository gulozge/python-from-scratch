from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        current = None

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1+val2
            carry = total//10
            data = total % 10

            new_node = ListNode(data)

            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head
