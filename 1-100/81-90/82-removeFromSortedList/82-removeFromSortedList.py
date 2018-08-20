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
        start = head
        prev = None
        flag = False
        
        while node:
            if node.val == start.val:
                start.next = node.next
                flag = True
            else:
                if flag:
                    if prev:
                        prev.next = node
                    else:
                        head = node
                else:
                    prev = start
                    
                start = node
                flag = False
            node = start.next
        
        if flag:
            if prev:
                prev.next = node
            else:
                head = node
        return head