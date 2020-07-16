import Queue
import heapq
import itertools

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        pairs = []

        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if i + j >= k:
                    break

                pairs.append((num1+num2, num1, num2))

        return map(lambda x: [x[1], x[2]], heapq.nsmallest(k, pairs))

    def kSmallestPairs2(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        if not nums1 or not nums2:
            return []

        length1, length2 = len(nums1), len(nums2)
        candidates = [(nums1[i] + nums2[0], i, 0) for i in range(length1)]
        heapq.heapify(candidates)
        result = []
        counter = itertools.count()

        while next(counter) < k and candidates:
            value, i, j = heapq.heappop(candidates)
            result.append((nums1[i], nums2[j]))

            if j + 1 < length2:
                heapq.heappush(candidates, (nums1[i] + nums2[j+1], i, j+1))

        return result