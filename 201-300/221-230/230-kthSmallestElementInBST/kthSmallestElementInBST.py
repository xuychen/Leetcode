# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        return self.kthSmallestHelper(root, k)[0]

    def kthSmallestHelper(self, node, k):
        if not node:
            return node, k

        value, k = self.kthSmallestHelper(node.left, k)
        if not k:
            return value, k

        k -= 1
        if not k:
            return node.val, k

        return self.kthSmallestHelper(node.right, k)

class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        return self.helper(root, 1, k)[1]

    def helper(self, node, count, k):
        if not node:
            return count, None

        left_count, left_value = self.helper(node.left, count, k)
        value = (left_count == k) * node.val
        right_count, right_value = self.helper(node.right, left_count+1, k)
        return right_count, left_value or right_value or value