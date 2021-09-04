import bisect
import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """

        self.prefix = w[:]
        for i in range(1, len(w)):
            self.prefix[i] += self.prefix[i-1]

        self.MAX = self.prefix[-1]

    def pickIndex(self):
        """
        :rtype: int
        """

        return bisect.bisect(self.prefix, random.randrange(self.MAX))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()