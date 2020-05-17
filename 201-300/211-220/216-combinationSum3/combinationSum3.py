class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        return self.combinationSum3_helper(k, n)

    def combinationSum3_helper(self, k, n, prev_num=0, track=[]):
        if k == 1 and prev_num < n < 10:
            return [track+[n]]

        result = []
        for i in range(prev_num+1, 10):
            result += self.combinationSum3_helper(k-1, n-i, i, track+[i])

        return result