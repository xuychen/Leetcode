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
        
        node, ref = self.getLeaves(root, TreeNode(-float('inf')), TreeNode(float('inf')))
        if node and ref:
            self.swap(node, ref)
        
    def swap(self, left, right):
        tmp = left.val
        left.val = right.val
        right.val = tmp
        
    def get(self, func, node, ref):
        return func(node, self.get(func, node.left, ref), self.get(func, node.right, ref), key=lambda x: x.val if x else ref) \
                if node else None
        
    def getLeaves(self, node, minimum, maximum):
        if not node:
            return None, None
        
        if node.val < minimum.val:
            return self.get(min, node, minimum.val), minimum
        elif node.val > maximum.val:
            return self.get(max, node, maximum.val), maximum
        else:
            left, leftRef = self.getLeaves(node.left, minimum, node)
            right, rightRef = self.getLeaves(node.right, node, maximum)
            
            if left and right and left.val > rightRef.val and right.val < leftRef.val:
                self.swap(left, right)
                return None, None
            else:
                return left or right, leftRef or rightRef