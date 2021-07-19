class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        MOD = 10 ** 9 + 7
        star_dict = {}
        star_dict["**"] = 15

        for i in range(10):
            if i == 1:
                star_dict[str(i)+"*"] = 9
            elif i == 2:
                star_dict[str(i)+"*"] = 6
            else:
                star_dict[str(i)+"*"] = 0

            if i <= 6:
                star_dict["*"+str(i)] = 2
            else:
                star_dict["*"+str(i)] = 1

        length = len(s)
        dp = [0] * (length + 1)
        dp[-1] = 1
        dp[length-1] = 9 if s[-1] == "*" else int(s[-1] != "0")

        for i in range(length-2, -1, -1):
            num = s[i: i+2]
            if num in star_dict:
                dp[i] = (dp[i] + dp[i+2] * star_dict[num]) % MOD
            elif 10 <= int(num) <= 26:
                dp[i] += (dp[i] + dp[i+2]) % MOD

            if num[0] == "*":
                dp[i] = (dp[i] + dp[i+1] * 9) % MOD
            elif int(num[0]) > 0:
                dp[i] = (dp[i] + dp[i+1]) % MOD

        return dp[0]