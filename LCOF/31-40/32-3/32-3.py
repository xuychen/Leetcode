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
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = []
        level = 0
        queue = Queue.Queue(maxsize=0)
        queue2 = Queue.Queue(maxsize=0)
        queue2.put(root)

        while not queue2.empty():
            queue, queue2 = queue2, queue
            level += 1
            level_result = []
            while not queue.empty():
                node = queue.get()
                level_result.append(node.val)
                if node.left:
                    queue2.put(node.left)
                if node.right:
                    queue2.put(node.right)

            result.append(level_result if level & 1 else level_result[::-1])

        return result