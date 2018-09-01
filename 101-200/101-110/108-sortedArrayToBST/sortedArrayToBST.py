# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        self.nums = nums
        return self.sortedArrayToBSTHelper(0, len(nums))
        
    def sortedArrayToBSTHelper(self, start, end):
        if start == end:
            return None
        
        mid = (start + end) / 2
        node = TreeNode(self.nums[mid])
        node.left = self.sortedArrayToBSTHelper(start, mid)
        node.right = self.sortedArrayToBSTHelper(mid+1, end)
        return node