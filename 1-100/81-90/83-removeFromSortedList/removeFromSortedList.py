# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head.next if head else None
        prev = head

        while node:
            if node.val == prev.val:
                prev.next = node.next
            else:
                prev = node

            node = prev.next

        return head

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        start = end = head

        while end:
            if start.val != end.val:
                start.next = end
                start = start.next

            end = end.next

        if start != end:
            start.next = end

        return head