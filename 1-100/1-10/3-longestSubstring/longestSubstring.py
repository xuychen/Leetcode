class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        index = 0
        result = 0
        count = 0
        cutline = -1
        dictionary = {}

        while index < len(s):
            chr = s[index]
            oldIndex = dictionary.get(chr, -1)
            if oldIndex == -1 or cutline >= oldIndex:
                dictionary[chr] = index
                count += 1
            else:
                if result < count:
                    result = count

                count = index - dictionary[chr]
                cutline = dictionary[chr]
                dictionary[chr] = index

            index += 1

        if count > result:
            result = count
        return result

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0
        charset = {}
        max_length = 0

        for end in range(len(s)):
            if charset.get(s[end], -1) < start:
                charset[s[end]] = end
                max_length = max(max_length, end-start+1)
            else:
                start = charset[s[end]] + 1
                charset[s[end]] = end

        return max_length