from collections import defaultdict

class Solution(object):
    def square_distance(self, point1, point2):
        xi, yi = point1
        xj, yj = point2
        return (xi-xj)**2 + (yi-yj)**2

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        map_points = sorted(map(tuple, points))
        target = defaultdict(lambda: defaultdict(int))
        length = len(points)
        result = 0

        for i in range(length):
            for j in range(i+1, length):
                dis = self.square_distance(map_points[i], map_points[j])
                result += target[map_points[i]][dis] * 2 + target[map_points[j]][dis] * 2
                target[map_points[i]][dis] += 1
                target[map_points[j]][dis] += 1

        return result