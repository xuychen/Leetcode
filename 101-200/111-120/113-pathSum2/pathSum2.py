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
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        if not root.left and not root.right:
            return [path + [root.val]] if sum == root.val else []
        
        return self.pathSum(root.left, sum-root.val, path+[root.val]) + self.pathSum(root.right, sum-root.val, path+[root.val])