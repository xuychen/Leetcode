# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return bool(self.getDepth(root, 1))
        
    def getDepth(self, node, level):
        if not node:
            return level
        
        lLevel, rLevel = self.getDepth(node.left, level+1), self.getDepth(node.right, level+1)
        return lLevel and rLevel and -1 <= lLevel - rLevel <= 1 and max(lLevel, rLevel)