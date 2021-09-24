class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        left, right = 0, 19

        while left <= right:
            mid = left + (right - left) / 2
            if 3 ** mid == n:
                return True
            elif 3 ** mid > n:
                right = mid - 1
            else:
                left = mid + 1

        return False

    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n > 1 and n % 3 == 0:
            n /= 3

        return n == 1