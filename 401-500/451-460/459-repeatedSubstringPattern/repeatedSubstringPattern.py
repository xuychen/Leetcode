class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        length = len(s)
        kmp = [0] * length

        j = 0
        for i in range(1, length):
            while j > 0 and s[i] != s[j]:
                j = kmp[j-1]

            j += 1 if s[i] == s[j] else 0
            kmp[i] = j

        return kmp[-1] and not kmp[-1] % (length-kmp[-1])

    # smart solution from others
    def repeatedSubstringPattern2(self, s):
        """
        :type s: str
        :rtype: bool
        """

        ss = (s + s)[1:-1]
        return ss.find(s) != -1