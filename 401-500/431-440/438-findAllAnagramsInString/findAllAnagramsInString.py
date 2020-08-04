class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        result = []
        s_len, p_len = len(s), len(p)
        counter = Counter(p)
        c_length = len(counter)

        if s_len < p_len:
            return []

        for i in range(p_len):
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                c_length -= 1

        if c_length == 0:
            result.append(i-p_len+1)

        for i in range(p_len, s_len):
            counter[s[i-p_len]] += 1
            if counter[s[i-p_len]] == 1:
                c_length += 1

            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                c_length -= 1

            if c_length == 0:
                result.append(i-p_len+1)

        return result