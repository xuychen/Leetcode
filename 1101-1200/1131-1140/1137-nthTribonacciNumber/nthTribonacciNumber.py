class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return int(bool(n))

        t1, t2, t3 = 0, 1, 1
        for i in range(2, n):
            t4 = t1 + t2 + t3
            t1, t2, t3 = t2, t3, t4

        return t4