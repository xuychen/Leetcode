# one liner

class Solution:
    def isValidBST(self, node, minimum=-float('inf'), maximum=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return not node or \
                (minimum < node.val < maximum and self.isValidBST(node.left, minimum, node.val) \
                and self.isValidBST(node.right, node.val, maximum))