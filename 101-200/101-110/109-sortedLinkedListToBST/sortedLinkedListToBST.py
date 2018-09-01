# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head, end=None):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        if head == end:
            return None
        
        mid = self.findMiddle(head, end)
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head, mid)
        node.right = self.sortedListToBST(mid.next, end)
        return node
            
    def findMiddle(self, start, end):
        fast = slow = start
        while fast != end:
            fast = fast.next
            if fast != end:
                slow = slow.next
                fast = fast.next
        return slow
        