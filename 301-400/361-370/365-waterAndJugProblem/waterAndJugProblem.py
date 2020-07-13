class Solution(object):
    def gcd(self, x, y):
        while y:
            x, y = y, x % y

        return x

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        return not z or (x + y >= z and not z % self.gcd(x, y))