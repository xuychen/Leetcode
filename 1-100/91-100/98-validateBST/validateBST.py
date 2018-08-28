# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.getLeaves(root, -float('inf'), float('inf'))[1]
    
    def getLeaves(self, node, minimum, maximum):
        if not node:
            return None, True
        
        left, resL = self.getLeaves(node.left, minimum, node.val)
        right, resR = self.getLeaves(node.right, node.val, maximum)
        return node.val, (resL and (left == None or (left < node.val and left > minimum))) and \
                        (resR and (right == None or (right < maximum and right > node.val)))