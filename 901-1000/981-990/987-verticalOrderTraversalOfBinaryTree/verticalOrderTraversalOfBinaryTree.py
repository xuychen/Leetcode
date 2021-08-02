import Queue
from collections import defaultdict
import operator

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        qe = Queue.Queue(maxsize=0)
        qe.put((root, 0, 0))
        lists = defaultdict(list)
        result = []

        while not qe.empty():
            node, level, index = qe.get()
            if node.left:
                qe.put((node.left, level+1, index-1))
            if node.right:
                qe.put((node.right, level+1, index+1))

            while len(lists[index]) <= level:
                lists[index].append([])

            lists[index][level].append(node.val)

        for key in sorted(lists.keys()):
            result.append(reduce(operator.__add__, map(sorted, lists[key])))

        return result