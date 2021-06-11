class Solution(object):
    def __init__(self):
        self.memory = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in self.memory:
            return self.memory[n]
        if n <= 1:
            return n

        result = int((self.fib(n-1) + self.fib(n-2)) % (1e9+7))
        self.memory[n] = result
        return result