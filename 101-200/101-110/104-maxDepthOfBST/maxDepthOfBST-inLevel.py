# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        queue = []
        level = 0
        queueFront = queueBack = 0

        if root:
            queue.append(root)
            queueFront += 1
            level += 1

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
                level += 1

        return level

    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1