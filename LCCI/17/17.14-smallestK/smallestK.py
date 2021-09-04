import heapq

class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        return heapq.nsmallest(k, arr)