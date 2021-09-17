# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.helper(root)[1]

    def helper(self, node):
        if not node:
            return 0, 0

        left_sum, left_tilt = self.helper(node.left)
        right_sum, right_tilt = self.helper(node.right)
        return left_sum + right_sum + node.val, left_tilt + right_tilt + abs(left_sum - right_sum)