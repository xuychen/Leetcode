# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        result = None
        for _ in range(k):
            result = stack.pop()

        return result

    def getKthFromEnd2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        fast = slow = head
        for _ in range(k):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow