# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        return bool(root and self.findSum(root, sum))
        
        
    def findSum(self, node, sum):
        if node and sum == node.val and not node.left and not node.right:
            return True
        
        return node and (self.findSum(node.left, sum-node.val) or self.findSum(node.right, sum-node.val))