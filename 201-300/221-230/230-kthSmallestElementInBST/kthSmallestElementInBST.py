# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        return self.kthSmallestHelper(root, k)[0]

    def kthSmallestHelper(self, node, k):
        if not node:
            return node, k

        value, k = self.kthSmallestHelper(node.left, k)
        if not k:
            return value, k

        k -= 1
        if not k:
            return node.val, k

        return self.kthSmallestHelper(node.right, k)