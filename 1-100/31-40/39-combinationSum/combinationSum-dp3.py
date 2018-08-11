# subtracting type dp with sort
class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        dp = [[[]]] + [[] for i in xrange(target)]
        for i in xrange(1, target + 1):
            for number in candidates:
                if number > i:
                    break
                for L in dp[i - number]:
                    if not L or number >= L[-1]:
                        dp[i] += L + [number],
        return dp[target]
