# subtracting type dp without sort
class Solution(object):
    def combinationSum(self, candidates, target):
        dp = [[[]]] + [[] for i in range(target)]
        for i in xrange(1, target + 1):
            for number in candidates:
                if number <= i:
                    for L in dp[i - number]:
                        if not L or number >= L[-1]:
                            dp[i] += L + [number],
        return dp[-1]