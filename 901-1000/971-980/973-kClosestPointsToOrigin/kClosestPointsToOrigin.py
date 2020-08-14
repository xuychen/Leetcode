import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        return heapq.nsmallest(K, points, key=lambda x: x[0] ** 2 + x[1] ** 2)