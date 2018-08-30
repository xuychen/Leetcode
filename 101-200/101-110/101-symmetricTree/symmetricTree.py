# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        queue = []
        queue.append(root)
        queueFront, queueBack = 1, 0
        
        while queueBack < queueFront:
            increase = 0
            while queueBack < queueFront:
                node = queue[queueBack]
                queueBack += 1
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    increase += 2
            queueFront += increase
            for index in range((queueFront-queueBack)/2):
                first, last = queue[queueBack+index], queue[queueFront-index-1]
                if (first and last and first.val != last.val) or ((not first) ^ (not last)):
                    return False
                
        return True