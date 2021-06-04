from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        lines = defaultdict(int)
        length = len(points)

        for i in range(length):
            x1, y1 = points[i]
            for j in range(i+1, length):
                x2, y2 = points[j]
                if x1 != x2:
                    slope = (y2-y1) / float((x2-x1))
                    intercept = y1 - slope * x1
                else:
                    slope = float('inf')
                    intercept = float('inf')

                lines[(x1, y1, slope, intercept)] += 1

        return max(lines.values() or [0]) + 1