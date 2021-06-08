# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.helper(root)[1] - 1

    def helper(self, node):
        if not node:
            return 0, 0

        left_max, left_path_max = self.helper(node.left)
        right_max, right_path_max = self.helper(node.right)
        return max(left_max, right_max) + 1, max(left_path_max, right_path_max, left_max+right_max+1)
        