from collections import Counter

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

class Solution2(object):
    def comparison(self, x, y):
        if x[1] == y[1]:
            return cmp(x[0], y[0])

        return -cmp(x[1], y[1])

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        return "".join(map(lambda x: x[0]*x[1], sorted(Counter(s).items(), self.comparison)))