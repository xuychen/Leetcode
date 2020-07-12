import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = collections.Counter(nums)
        count2int = collections.defaultdict(list)
        result = []

        for key, value in counter.items():
            count2int[value].append(key)

        for count in heapq.nlargest(k, counter.values()):
            result.append(count2int[count].pop())

        return result