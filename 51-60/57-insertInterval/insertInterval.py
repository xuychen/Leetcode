# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        return self.merge(intervals + [newInterval])
        
        
    def comparator(self, key):
        return key.start
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        intervals.sort(key=self.comparator)
        prev, endIndex = (intervals[0], 1) if intervals else (None, 0)
            
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start > prev.end:
                prev = intervals[endIndex] = interval
                endIndex += 1
            else:
                prev.end = max(prev.end, interval.end)
        
        return intervals[:endIndex]