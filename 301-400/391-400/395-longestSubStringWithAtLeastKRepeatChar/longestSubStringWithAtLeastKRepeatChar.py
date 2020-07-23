class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        notchar = set()
        start = 0
        length = len(s)
        result = 0

        if k <= 1:
            return length

        while start < length:
            if s[start] not in notchar:
                end = start
                counter = {}
                match = 0
                total = 0
                while end < length:
                    if s[end] not in counter:
                        counter[s[end]] = 1
                        total += 1
                    else:
                        counter[s[end]] += 1
                        if counter[s[end]] == k:
                            match += 1
                        if match == total:
                            result = max(result, end - start + 1)

                    end += 1

                for key, value in counter.items():
                    if value < k:
                        notchar.add(key)

            start += 1

        return result

                