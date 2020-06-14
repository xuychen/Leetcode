# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        return self.binaryTreePathsHelper(root, "") if root else []

    def binaryTreePathsHelper(self, node, track):
        result = []
        track += "->" * bool(track) + str(node.val)
        if not node.left and not node.right:
            return [track]
        if node.left:
            result += self.binaryTreePathsHelper(node.left, track)
        if node.right:
            result += self.binaryTreePathsHelper(node.right, track)

        return result