class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        length = len(s)
        result = ""
        count = 0

        for i in range(length-1, -1, -1):
            if s[i].isalpha():
                result += s[i].upper()
                count += 1
            elif s[i].isnumeric():
                result += s[i]
                count += 1

            if count == k:
                result += '-'
                count = 0

        return result[-2::-1] if result and result[-1] == "-" else result[::-1]
