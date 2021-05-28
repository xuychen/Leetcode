class Solution(object):
    def dfs(self, node, dp, words):
        if node == -1:
            return [words[1:-1]]
        return sum([self.dfs(pair[1], dp, words + " " + pair[0]) for pair in dp[node]], [])

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        length = len(s)
        dp = [[] for _ in range(length + 1)]
        dp[-1].append(("", -1))

        for i in range(length, 0, -1):
            if dp[i]:
                for word in wordDict:
                    if s.endswith(word, 0 , i):
                        dp[i - len(word)].append((word, i))

        return self.dfs(0, dp, "")

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        length = len(s)
        dp = [[] for _ in range(length+1)]
        dp[0].append("")

        for i in range(length):
            if dp[i]:
                for word in wordDict:
                    if s.startswith(word, i):
                        for lhs in dp[i]:
                            dp[i + len(word)].append(lhs+" "+word if lhs else word)

        return dp[-1]