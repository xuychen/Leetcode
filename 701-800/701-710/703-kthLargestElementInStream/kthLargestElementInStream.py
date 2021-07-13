import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self.min_heap = []
        self.heap_size = 0
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heapq.heappush(self.min_heap, val)
        self.heap_size += 1

        if self.heap_size > self.k:
            self.heap_size -= 1
            heapq.heappop(self.min_heap)

        return self.min_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)