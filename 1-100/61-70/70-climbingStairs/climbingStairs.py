class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return n

        one_step_before, two_steps_before = 2, 1
        all_ways = 0

        for _ in range(3, n+1):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways

        return all_ways

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)
        dp[0] = 1

        while True:
            dp2 = [0] * (n + 1)
            dp2[-1] = dp[-1]

            for i in range(n):
                if i + 1 <= n:
                    dp2[i+1] += dp[i]
                if i + 2 <= n:
                    dp2[i+2] += dp[i]

            if dp == dp2:
                return dp2[-1]
            else:
                dp = dp2

        return 0