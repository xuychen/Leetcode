class Solution(object):
    def singleMatch(self, query, pattern):
        i, j, q_length, p_length = 0, 0, len(query), len(pattern)
        while i < p_length:
            while query[j] != pattern[i]:
                if j == q_length - 1 or query[j].isupper():
                    return False

                j = j + 1

            i, j = i + 1, j + 1

        for index in range(j, q_length):
            if (query[index].isupper()):
                return False

        return True

    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        return [self.singleMatch(query, pattern) for query in queries]
