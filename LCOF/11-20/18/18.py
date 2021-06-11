# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        prev, node = None, head
        while node and node.val != val:
            prev = node
            node = node.next

        if not prev:
            return head.next

        prev.next = node.next
        return head
