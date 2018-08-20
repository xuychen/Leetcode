# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        node = head
        leftHead = rightHead = left = right = None

        while node:
            if node.val < x:
                if left:
                    left.next = node
                else:
                    leftHead = node
                left = node
            else:
                if right:
                    right.next = node
                else:
                    rightHead = node
                right = node
            
            node = node.next
        
        if left:
            left.next = rightHead
        if right:
            right.next = None
        return leftHead if leftHead else rightHead