from collections import Counter
import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        candidates = Counter(nums).keys()
        return heapq.nlargest(3, candidates)[-1] if len(candidates) >= 3 else max(candidates)