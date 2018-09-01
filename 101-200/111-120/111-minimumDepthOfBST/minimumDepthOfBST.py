# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        depth = 0
        if not root:
            return depth
        
        queue = [root]
        while queue != []:
            newQueue = []
            depth += 1
            for elem in queue:
                if not (elem.left or elem.right):
                    return depth
                if elem.left:
                    newQueue.append(elem.left)
                if elem.right:
                    newQueue.append(elem.right)
            queue = newQueue
        return depth