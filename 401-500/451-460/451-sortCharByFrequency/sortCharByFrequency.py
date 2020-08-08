class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        chars = [[0, i] for i in range(128)]
        result = ""

        for char in s:
            chars[ord(char)][0] += 1

        chars.sort(key=lambda x: (-x[0], x[1]))

        for times, code in chars:
            if not times:
                break

            result += chr(code) * times

        return result