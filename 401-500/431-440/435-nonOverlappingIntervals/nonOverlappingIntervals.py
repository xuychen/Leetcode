class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        end = float('-inf')
        intervals.sort(key=lambda x: (x[1], x[0]))
        count = 0

        for interval in intervals:
            if end <= interval[0]:
                end = interval[1]
            else:
                count += 1
                
        return count