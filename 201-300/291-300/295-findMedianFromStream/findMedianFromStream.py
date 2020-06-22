import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.maxHeap = []
        self.minHeap = []
        self.maxHeapSize = 0
        self.minHeapSize = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if self.maxHeapSize == self.minHeapSize:
            if not self.maxHeapSize or num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)

            self.maxHeapSize += 1
        else:
            heapq.heappush(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            self.minHeapSize += 1

    def findMedian(self):
        """
        :rtype: float
        """

        return (self.minHeap[0] - self.maxHeap[0]) / 2.0 if self.minHeapSize == self.maxHeapSize else -self.maxHeap[0]


class MedianFinder2:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heapq.heappush(small, -heapq.hheappushpop(large, num))
        if len(large) < len(small):
            heapq.hheappush(large, -heapq.hheappop(small))

    def findMedian(self):
        small, large = self.heaps
        return (large[0] - small[0]) / 2.0 if len(large) == len(small) else large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()