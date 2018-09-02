# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
          
        return self.findPossibilities(root, sum, 0)[1]
        
    def findPossibilities(self, node, sum, count):
        if not node:
            return [], count
        
        result = []
        candidates1, candidates2 = self.findPossibilities(node.left, sum, count), self.findPossibilities(node.right, sum, count)
        for elem in [0] + candidates1[0] + candidates2[0]:
            if elem + node.val == sum:
                count += 1
            result.append(elem+node.val)
        return result, count + candidates1[1] + candidates2[1]