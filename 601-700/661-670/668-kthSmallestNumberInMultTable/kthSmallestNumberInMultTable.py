class Solution(object):
    def count(self, n_rows, n_cols, num):
        count = 0
        for i in range(1, n_rows+1):
            count += min(n_cols, num / i)

        return count

    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) / 2
            if (self.count(m, n, mid) < k):
                left = mid + 1
            else:
                right = mid

        return left
