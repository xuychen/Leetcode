# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root :
            return None

        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.right, root.left = left, right
        return root