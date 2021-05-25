# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if root:
            self.flattenHelper(root)

    def flattenHelper(self, node):
        tail = node
        right = node.right
        if node.left:
            node.right, tail = self.flattenHelper(node.left)
            node.left = None
        if right:
            tail.right, tail = self.flattenHelper(right)
        return node, tail