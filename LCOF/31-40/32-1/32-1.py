import Queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        queue = Queue.Queue(maxsize=0)
        queue.put(root)
        result = []

        while not queue.empty():
            node = queue.get()
            result.append(node.val)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

        return result
            