# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root, string=''):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return int(string or 0)
        if root.left and root.right:
            return self.sumNumbers(root.left, string+str(root.val)) + self.sumNumbers(root.right, string+str(root.val))
        
        return self.sumNumbers(root.left or root.right, string+str(root.val))