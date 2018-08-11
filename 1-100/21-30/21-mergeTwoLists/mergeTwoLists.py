# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = l1
        if l1 and l2:
            if l1.val > l2.val:
                tmp = l2.next
                l2.next = l1
                head = l2
                l2 = tmp
            else:
                l1 = l1.next
        
        prev = head
        
        while l1 and l2:
            if l1.val > l2.val:
                tmp = l2.next
                l2.next = prev.next
                prev.next = l2
                prev = l2
                l2 = tmp
            else:
                prev = l1
                l1 = l1.next
        
        if prev and not l1:
            prev.next = l2
        
        return head or l2