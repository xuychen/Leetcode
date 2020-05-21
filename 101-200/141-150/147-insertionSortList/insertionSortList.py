# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insert(self, head, new_node):
        if new_node.val < head.val:
            new_node.next = head
            return new_node

        node = head
        while node:
            if not node.next or new_node.val < node.next.val:
                new_node.next = node.next
                node.next = new_node
                break

            node = node.next

        return head

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        candidate = head.next
        head.next = None

        while candidate:
            next_candidate = candidate.next
            head = self.insert(head, candidate)
            candidate = next_candidate

        return head