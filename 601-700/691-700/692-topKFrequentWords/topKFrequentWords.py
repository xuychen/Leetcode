import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        counter = Counter(words)
        return heapq.nsmallest(k, counter.keys(), key=lambda x: (-counter[x], x))