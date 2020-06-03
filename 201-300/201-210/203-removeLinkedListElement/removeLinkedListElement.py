# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        prev, node = None, head

        while node:
            if node.val == val:
                if prev:
                    prev.next = node.next
                else:
                    head = node.next
            else:
                prev = node

            node = node.next

        return head