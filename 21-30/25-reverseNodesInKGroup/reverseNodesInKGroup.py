# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# recursion
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        start, nextOne, nextGroup = self.reverseInOrder(head, k, k-1)
        while nextGroup:
            nextOne.next, nextOne, nextGroup = self.reverseInOrder(nextGroup, k, k-1)     
        if nextOne:
            nextOne.next = None
        return start
        
    def reverseInOrder(self, head, k, kLeft):  
        if not head:
            return None, None, None
        
        if kLeft > 0:
            startPoint, nextOne, nextGroup = self.reverseInOrder(head.next, k, kLeft-1)
            if nextOne:
                nextOne.next = head
                nextOne = head
            else:
                startPoint = head
        elif kLeft == 0:
            nextOne = head
            startPoint = head
            nextGroup = head.next
    
        return startPoint, nextOne, nextGroup