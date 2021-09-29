from collections import Counter

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

class Solution2(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        return self.helper(root, targetSum)[1]

    def helper(self, node, targetSum):
        if not node:
            return {}, 0

        left_counter, left_count = self.helper(node.left, targetSum)
        right_counter, right_count = self.helper(node.right, targetSum)
        new_counter = Counter([node.val])

        for key, value in left_counter.items():
            new_counter[key+node.val] += value
        for key, value in right_counter.items():
            new_counter[key+node.val] += value

        return new_counter, new_counter[targetSum] + left_count + right_count