# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        result = self.helper(root)
        return result[1] if result and not result[0] else 0

    def helper(self, node):
        if not node:
            return None

        left = self.helper(node.left)
        right = self.helper(node.right)

        if not left and not right:
            return True, node.val

        return False, (left[1] if left else 0) + (right[1] if right and not right [0] else 0)