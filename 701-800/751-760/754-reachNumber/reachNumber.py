import math

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """

        target = abs(target)
        n = int(math.ceil((-1.0 + math.sqrt(1 + 8.0 * target)) / 2))
        diff = n * (n + 1) / 2 - target
        return n + (2 if n & 1 else 1) if diff & 1 else n