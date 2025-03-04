from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        tmp_list = list()

        for i in lists:
            tmp_list.extend(self.extract_values(i))
        tmp_list.sort()

        return self.create_linked_list(tmp_list)

    def create_linked_list(self, l1: list):
        head = None
        for i in l1:
            new_node = ListNode(i)
            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
        return head

    def extract_values(self, head):
        values = list()
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values
