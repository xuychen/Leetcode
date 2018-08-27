# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        return self.getSmallerTree(1, n+1) if n else []
    
    def getSmallerTree(self, start, end):
        result = []
        for i in range(start, end):
            left, right = self.getSmallerTree(start, i), self.getSmallerTree(i+1, end)
            for eachleft in left:
                for eachright in right:
                    root = TreeNode(i)
                    root.left, root.right = eachleft, eachright
                    result.append(root)
        
        return result or [None]