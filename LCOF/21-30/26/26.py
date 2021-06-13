# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_node(self, node, val):
        if not node:
            return []

        return self.find_node(node.left, val) + ([node] if node.val == val else []) + self.find_node(node.right, val)

    def tree_comparison(self, o_node, p_node):
        if not p_node:
            return True
        if not o_node or o_node.val != p_node.val:
            return False

        return self.tree_comparison(o_node.left, p_node.left) and self.tree_comparison(o_node.right, p_node.right)

    def isSubStructure(self, tree_a, tree_b):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        if not tree_b:
            return False

        for start_node in self.find_node(tree_a, tree_b.val):
            if self.tree_comparison(start_node, tree_b):
                return True

        return False