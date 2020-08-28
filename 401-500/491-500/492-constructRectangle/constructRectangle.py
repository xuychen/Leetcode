class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        for i in range(int(area ** 0.5), 0, -1):
            if not area % i:
                return [area / i, i]