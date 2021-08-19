# dp solution from discussion.
from collections import defaultdict

cache = {}
class Solution(object):
    def countArrangement(self, N):
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in xrange(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))

class Solution2(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        candidates = defaultdict(list)

        for i in range(1, n+1):
            for j in range(i, n+1):
                if i % j == 0 or j % i == 0:
                    candidates[i].append(j)
                    if i != j:
                        candidates[j].append(i)

        masked = (1 << n) - 1
        return self.dfs(candidates, 1, n, masked)

    def dfs(self, candidates, value, n, mask):
        if value > n:
            return mask == 0

        count = 0
        for candidate in candidates[value]:
            if mask & (1 << (candidate-1)):
                count += self.dfs(candidates, value+1, n, mask ^ 1 << (candidate-1))

        return count