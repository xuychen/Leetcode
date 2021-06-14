import Queue
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

        if not root:
            return True

        queue = Queue.Queue(maxsize=0)
        queue2 = Queue.Queue(maxsize=0)
        queue2.put(root.left)
        queue2.put(root.right)

        while not queue2.empty():
            queue, queue2 = queue2, queue
            while not queue.empty():
                node1 = queue.get()
                node2 = queue.get()
                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                queue2.put(node1.left)
                queue2.put(node2.right)
                queue2.put(node1.right)
                queue2.put(node2.left)

        return True
            