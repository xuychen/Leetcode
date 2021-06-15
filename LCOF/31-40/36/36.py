"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return None

        head, tail = self.helper(root)
        head.left = tail
        tail.right = head
        return head

    def helper(self, node):
        head = tail = node
        if node.left:
            head, node.left = self.helper(node.left)
            node.left.right = node
        if node.right:
            node.right, tail = self.helper(node.right)
            node.right.left = node

        return head, tail