class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True

        for i in range(length):
            if dp[i]:
                for word in wordDict:
                    if s.startswith(word, i):
                        dp[i + len(word)] = True

        return dp[-1]