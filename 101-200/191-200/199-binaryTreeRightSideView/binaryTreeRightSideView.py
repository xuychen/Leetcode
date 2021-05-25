import Queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def helper(self, node, track, depth=0):
        if not node:
            return
        if depth == len(track):
            track.append(node.val)

        self.helper(node.right, track, depth+1)
        self.helper(node.left, track, depth+1)


    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        track = []
        self.helper(root, track)
        return track

    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        queue = Queue.Queue(maxsize=0)
        queue2 = Queue.Queue(maxsize=0)
        queue2.put(root)
        result = []
        lastnum = 0

        if not root:
            return result

        while not queue2.empty():
            queue, queue2 = queue2, queue
            while not queue.empty():
                node = queue.get()
                lastnum = node.val
                if node.left:
                    queue2.put(node.left)
                if node.right:
                    queue2.put(node.right)

            result.append(lastnum)

        return result