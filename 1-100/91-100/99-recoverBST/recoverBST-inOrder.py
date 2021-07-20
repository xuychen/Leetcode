# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        pair = self.recoverTreeHelper(root, TreeNode(-float('inf')), None)[0]
        if pair:
            self.swap(pair[0], pair[1])

    def swap(self, left, right):
        tmp = left.val
        left.val = right.val
        right.val = tmp

    def recoverTreeHelper(self, node, prev, pair):
        if node:
            pair, prev = self.recoverTreeHelper(node.left, prev, pair)
            pair2 = (prev, node) if prev.val > node.val else None
            if pair and pair2:
                self.swap(pair[0], pair2[1])
                return None, prev
            else:
                return self.recoverTreeHelper(node.right, node, pair or pair2)
        return pair, prev

class Solution2(object):
    def get_inorder(self, node):
        if not node:
            return []

        return self.get_inorder(node.left) + [node] + self.get_inorder(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        preorder = self.get_inorder(root)
        prev = TreeNode(float('-inf'))
        first_node = second_node = None

        for node in preorder:
            if prev.val > node.val:
                if not first_node:
                    first_node = prev
                    second_node = node
                else:
                    second_node = node

            prev = node

        first_node.val, second_node.val = second_node.val, first_node.val
