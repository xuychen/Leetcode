class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        count = 0
        pattern = [float('-inf')] * 2

        for point in sorted(points):
            if point[0] <= pattern[1]:
                pattern[0], pattern[1] = max(pattern[0], point[0]), min(pattern[1], point[1])
            else:
                pattern[0], pattern[1] = point[0], point[1]
                count += 1

        return count