# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """

        return self.helper(root, target, [])

    def helper(self, node, target, path):
        if not node:
            return []
        if target == node.val and not node.left and not node.right:
            return [path+[node.val]]

        return self.helper(node.left, target-node.val, path+[node.val]) + self.helper(node.right, target-node.val, path+[node.val])        