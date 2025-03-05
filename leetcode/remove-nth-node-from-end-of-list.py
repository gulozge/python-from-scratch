from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp_list = list()
        current = head

        while current:
            tmp_list.append(current.val)
            current = current.next

        tmp_list.pop(len(tmp_list) - n)

        head = None
        for i in tmp_list:
            new_node = ListNode(i)
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next

        return head
