from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        current = head
        while current:
            seen.add(current.val)
            current = current.next

        seen = list(seen)
        seen.sort()
        head = None
        for i in seen:
            new_node = ListNode(i)
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
        return head
