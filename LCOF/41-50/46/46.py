class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """

        str_num = str(num)
        length = len(str_num)
        dp = [0] * (length + 1)
        dp[-1] = 1

        for i in range(length-1, -1, -1):
            if 10 <= int(str_num[i:i+2]) < 26:
                dp[i] += dp[i+2]

            dp[i] += dp[i+1]

        return dp[0]

    def translateNum2(self, num):
        """
        :type num: int
        :rtype: int
        """

        dp1 = dp2 = dp3 = 1
        while num > 0:
            if 10 <= num % 100 < 26:
                dp3 += dp1

            dp1, dp2 = dp2, dp3
            num /= 10

        return dp3