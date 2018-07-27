# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def buildChildTree(inIndex, postIndex, length):
            if length == 0:
                return None

            root = TreeNode(postorder[postIndex])
            count = 0
            while inorder[inIndex+count] != postorder[postIndex]:
                count += 1
            root.left = buildChildTree(inIndex, postIndex-length+count, count)
            root.right = buildChildTree(inIndex+count+1, postIndex-1, length-count-1)
            return root
        
        return buildChildTree(0, len(postorder)-1, len(postorder))