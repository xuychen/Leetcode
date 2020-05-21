# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        visited = set()
        nodeA, nodeB = headA, headB

        while nodeA:
            visited.add(nodeA)
            nodeA = nodeA.next

        while nodeB:
            if nodeB in visited:
                return nodeB

            nodeB = nodeB.next

        return None