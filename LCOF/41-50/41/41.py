import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.min_heap = []
        self.max_heap = []
        self.min_size = 0
        self.max_size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if self.min_size == self.max_size:
            if not self.max_size or -self.max_heap[0] > num:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

            self.max_size += 1
        else:
            if -self.max_heap[0] < num:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

            self.min_size += 1



    def findMedian(self):
        """
        :rtype: float
        """

        if self.min_size == self.max_size:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()