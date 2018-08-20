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