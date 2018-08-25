# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        prev, node = None, head
        i = 0
        for i in range(1, m):
            prev = node
            node = node.next
        
        reverseHead, _ = self.reverse(node, None, n-i, n-i)
        if prev:
            prev.next = reverseHead
        else:
            head = reverseHead
            
        return head
        
    def reverse(self, node, prev, index, count):
        if index == 0:
            return prev, node
        
        reverseHead, tailHead = self.reverse(node.next, node, index-1, count)
        node.next = prev if index != count else tailHead
        return reverseHead, tailHead