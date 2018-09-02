# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum, path=[]):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        if not root:
            return 0
        return int(sum == root.val) + self.pathSum(root.left, sum-root.val, path+[root.val]) + \
                self.pathSum(root.right, sum-root.val, path+[root.val]) + (self.pathSum(root.left, sum, path) + \
                self.pathSum(root.right, sum, path) if path == [] else 0)