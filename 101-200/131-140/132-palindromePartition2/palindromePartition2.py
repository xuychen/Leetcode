class Solution(object):
    def is_palindrome(self, s, left, right):
        while (left <= right):
            if (s[left] != s[right]):
                return False
            else:
                left += 1
                right -= 1

        return True

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        dp = [length] * (length + 1)

        dp[-1] = 0
        dp[-2] = 1

        for size in range(2, length+1):
            for index in range(1, size+1):
                if dp[length-size] > dp[length-size+index] + 1:
                    dp[length-size] = (dp[length-size+index] + 1) if self.is_palindrome(s, length-size, length-size+index-1) else dp[length-size]

        return dp[0] - 1