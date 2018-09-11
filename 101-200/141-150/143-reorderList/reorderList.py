# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        self.merge(head, self.reverse(self.middle(head)))
        
    def middle(self, head):
        if not head or not head.next:
            return head
        
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        return slow
    
    def reverse(self, head):
        node = None
        nextNode = head
        while nextNode:
            tmp = nextNode.next
            nextNode.next = node
            node = nextNode
            nextNode = tmp
        return node
            
    def merge(self, list1, list2):
        while list1:
            tmp = list1.next
            list1.next = list2
            list1 = list2
            list2 = tmp