# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def buildChildTree(preIndex, inIndex, length):
            if length == 0:
                return None

            root = TreeNode(preorder[preIndex])
            count = 0
            while inorder[inIndex+count] != preorder[preIndex]:
                count += 1

            root.left = buildChildTree(preIndex+1, inIndex, count)
            root.right = buildChildTree(preIndex+count+1, inIndex+count+1, length-count-1)
            return root

        return buildChildTree(0, 0, len(preorder))

    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root