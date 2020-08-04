class Solution(object):
    def findRightInterval(self, intervals):
        starts = sorted([I[0], i] for i, I in enumerate(intervals)) + [[float('inf'), -1]]
        return [starts[bisect.bisect(starts, [I[-1]])][1] for I in intervals]

        