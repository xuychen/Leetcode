# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        queue = []
        result = []
        queueFront = queueBack = 0
        reverse = True
        
        if root:
            queue.append(root)
            queueFront += 1
            result.append([root.val])
        
        while queueBack < queueFront:
            increase = 0
            while queueBack < queueFront:
                node = queue[queueBack]
                queueBack += 1
                if node.left:
                    queue.append(node.left)
                    increase += 1
                if node.right:
                    queue.append(node.right)
                    increase += 1
            if increase:
                queueFront += increase
                result.append(map(lambda x: x.val, queue[queueFront-1: queueBack-1: -1] if reverse else queue[queueBack: queueFront]))
                reverse = not reverse
        
        return result