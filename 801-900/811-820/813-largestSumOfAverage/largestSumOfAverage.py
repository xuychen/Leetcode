class Solution(object):
    def largestSumOfAverages(self, A, K):
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        P = [0]
        for x in A:
            P.append(P[-1] + x)

        N = len(A)
        dp = [average(i, N) for i in xrange(N)]
        for k in xrange(K-1):
            for i in xrange(N):
                for j in xrange(i+1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/largest-sum-of-averages/solution/zui-da-ping-jun-zhi-he-de-fen-zu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。