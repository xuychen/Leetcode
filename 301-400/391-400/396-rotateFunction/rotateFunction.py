class Solution(object):
    def maxRotateFunction(self, a):
        """
        :type A: List[int]
        :rtype: int
        """

        summation = sum(a)
        length = len(a)
        func = sum([i * value for i, value in enumerate(a)])
        result = func

        while a:
            func += summation - length * a.pop()
            result = max(result, func)

        return result