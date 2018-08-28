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