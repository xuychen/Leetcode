# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return bool(self.getDepth(root, 1))

    def getDepth(self, node, level):
        if not node:
            return level

        lLevel, rLevel = self.getDepth(node.left, level+1), self.getDepth(node.right, level+1)
        return lLevel and rLevel and -1 <= lLevel - rLevel <= 1 and max(lLevel, rLevel)

class Solution2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.helper(root)[1]

    def helper(self, node):
        if not node:
            return 0, True

        left_height, left_balanced = self.helper(node.left)
        right_height, right_balanced = self.helper(node.right)

        if left_balanced and right_balanced:
            return max(left_height, right_height) + 1, abs(left_height-right_height) <= 1

        return max(left_height, right_height), False