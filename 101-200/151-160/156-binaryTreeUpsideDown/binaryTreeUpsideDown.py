# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None

        node = root
        left, right = node.left, node.right
        node.left, node.right = None, None

        while left:
            prev_node, prev_right = node, right
            node = left
            left, right = node.left, node.right
            node.left = prev_right
            node.right = prev_node

        return node