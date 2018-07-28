# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursion
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        return head if self.removeByRecursion(head, n) == n + 1 else head.next

    def removeByRecursion(self, node, n):
        if node == None:
            return 0

        reverseIndex = self.removeByRecursion(node.next, n) + 1

        if reverseIndex == n + 1:
            node.next = node.next.next
        elif reverseIndex > n + 1:
            reverseIndex -= 1

        return reverseIndex
            