class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        length = len(s)
        i = 0
        result = ""

        while i * 2 * k < length:
            result += s[i*2*k:i*2*k+k][::-1] + s[i*2*k+k:(i+1)*2*k]
            i += 1

        return result