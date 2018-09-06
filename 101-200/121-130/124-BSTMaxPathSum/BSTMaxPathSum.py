# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.maximum = -float('inf')
        self.maxPathSumHelper(root)
        return self.maximum
    
    def maxPathSumHelper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return -float('inf')
        
        left, right = self.maxPathSumHelper(root.left), self.maxPathSumHelper(root.right)
        local = root.val + max(left, right, 0)

        if root.val >= 0:
            maximum = root.val + left + right if left > 0 and right > 0 else local
        else:
            maximum = max(root.val, left, right, root.val+left+right)
        self.maximum = max(maximum, self.maximum)
        return local