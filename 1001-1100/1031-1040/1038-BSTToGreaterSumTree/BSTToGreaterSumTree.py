# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.helper(root)
        return root

    def helper(self, node, summation = 0):
        if not node:
            return summation

        right = self.helper(node.right, summation)
        node.val += right
        left = self.helper(node.left, node.val)
        return left
