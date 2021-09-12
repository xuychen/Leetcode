import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """

        cap_profit = sorted(zip(capital, profits))
        length = len(cap_profit)
        array = []
        index = 0
        result = w

        for _ in range(min(k, length)):
            while index < length and cap_profit[index][0] <= result:
                heapq.heappush(array, -cap_profit[index][1])
                index += 1

            if array:
                result += -heapq.heappop(array)

        return result
