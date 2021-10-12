from collections import Counter

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        counter = Counter()

        for start, end in paths:
            counter[start] += 1
            counter[end] -= 1

        for key, value in counter.items():
            if counter[key] == -1:
                return key

        return None
