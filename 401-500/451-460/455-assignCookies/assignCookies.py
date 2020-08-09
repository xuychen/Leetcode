class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()
        glen, slen = len(g), len(s)
        i = j = 0

        while i < glen and j < slen:
            if g[i] <= s[j]:
                i += 1

            j += 1

        return i