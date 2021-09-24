# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        stack = []
        result = [None] * k

        node = head
        while node:
            stack.append(node)
            node = node.next

        length = len(stack)
        quotient = length / k
        remainder = length % k

        if not stack:
            return result

        for i in range(k-1, -1, -1):
            stack[-1].next = None
            if i < remainder:
                result[i] = stack.pop()

            for _ in range(quotient):
                result[i] = stack.pop()

        return result