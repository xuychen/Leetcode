# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node:
            result.append(node.val)
            self.helper(node.left, result)
            self.helper(node.right, result)
