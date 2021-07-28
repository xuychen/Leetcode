# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return -1

        result = self.helper(root, root.val)
        return result if result != float('inf') else -1

    def helper(self, node, target):
        if not node:
            return float('inf')
        if node.val != target:
            return node.val

        left = self.helper(node.left, target)
        right = self.helper(node.right, target)
        return min(float('inf') if node.val == target else node.val, left, right)