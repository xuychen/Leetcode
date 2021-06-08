class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if not prices or not k:
            return 0

        dp = [[0, 0] for _ in range(k)]
        for i in range(k):
            dp[i][0] = -prices[0]

        for price in prices:
            prev_sell = 0
            for i in range(k):
                dp[i][0] = max(dp[i][0], prev_sell-price)
                dp[i][1] = max(dp[i][1], dp[i][0]+price)
                prev_sell = dp[i][1]

        return dp[-1][1]