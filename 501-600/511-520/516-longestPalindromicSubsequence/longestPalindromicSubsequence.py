class Solution(object):
    def __init__(self):
        self.dp = {}

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        return self.helper(s, 0, len(s)-1)

    def helper(self, s, start, end):
        if (start, end) in self.dp:
            return self.dp[(start, end)]

        if start > end:
            result = 0
        elif start == end:
            result = 1
        elif s[start] == s[end]:
            result = self.helper(s, start+1, end-1) + 2
        else:
            left = self.helper(s, start+1, end)
            right = self.helper(s, start, end-1)
            result = max(left, right)

        self.dp[(start, end)] = result
        return result