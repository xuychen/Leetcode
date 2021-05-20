import operator

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        period = (numRows - 1) * 2
        result = ""
        end = ""
        length = len(s)

        i = 0
        while i * period < length:
            result += s[i*period]
            if i * period + numRows - 1< length:
                end += s[i * period + numRows - 1]
            i += 1


        for i in range(1, numRows-1):
            j = 0
            while j * period < length:
                lowerBase = j * period
                upperBase = lowerBase + period
                if (lowerBase + i < length):
                    result += s[lowerBase+i]
                    if (upperBase - i < length):
                        result += s[upperBase-i]

                j += 1

        return result + end

    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        num_groups = 2 * (numRows - 1)
        strings = [""] * numRows

        for i in range(len(s)):
            mod = i % num_groups
            if mod > num_groups / 2:
                strings[num_groups-mod] += s[i]
            else:
                strings[mod] += s[i]

        return reduce(operator.__add__, strings)