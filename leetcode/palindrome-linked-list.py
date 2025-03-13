from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        current = head
        while current:
            tmp.append(current.val)
            current = current.next
        if tmp == tmp[::-1]:
            return True
        else:
            return False
