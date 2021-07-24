import Queue
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_width = 0
        qe = Queue.Queue(maxsize=0)
        alter_qe = Queue.Queue(maxsize=0)
        qe.put((1, root))

        while not qe.empty():
            width = 0
            start_index = -1
            while not qe.empty():
                index, elem = qe.get()

                if elem:
                    if start_index == -1:
                        start_index = index

                    alter_qe.put((2 * index - 1, elem.left))
                    alter_qe.put((2 * index, elem.right))
                    width = index - start_index + 1

            max_width = max(max_width, width)
            qe, alter_qe = alter_qe, qe

        return max_width

    def widthOfBinaryTree2(self, root):
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [kid
                    for number, node in level
                    for kid in enumerate((node.left, node.right), 2 * number)
                    if kid[1]]
        return width

class Solution2(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        qe = deque()
        qe.append((root, 1, 0))
        minimum, maximum = float('inf'), float('-inf')
        level = 1
        result = 0

        while qe:
            if qe[0][1] == level:
                node, lvl, index = qe.popleft()
                if node:
                    minimum = min(minimum, index)
                    maximum = max(maximum, index)
                    qe.append((node.left, lvl+1, index*2))
                    qe.append((node.right, lvl+1, index*2+1))
                    result = max(result, maximum - minimum + 1)
            else:
                minimum, maximum = float('inf'), float('-inf')
                level += 1

        return result
