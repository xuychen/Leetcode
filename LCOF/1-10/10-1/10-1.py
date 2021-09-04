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

    # 矩阵快速幂
    def fib2(self, n):
        MOD = 10 ** 9 + 7
        if n < 2:
            return n

        def multiply(a, b):
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
                    
            return c

        def matrix_pow(a, n):
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n - 1)
        return res[0][0]
