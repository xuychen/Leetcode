# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root, value=1):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        return max(self.countNodes(root.left, value*2), self.countNodes(root.right, value*2+1), value)