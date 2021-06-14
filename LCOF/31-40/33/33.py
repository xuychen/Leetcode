import bisect

class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """

        if len(postorder) <= 1:
            return True

        root = postorder.pop()
        index = bisect.bisect(postorder, root)
        left, right = postorder[:index], postorder[index:]
        return not filter(lambda x: x > root, left) and not filter(lambda x: x < root, right) and self.verifyPostorder(left) and self.verifyPostorder(right)