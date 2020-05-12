from random import randrange

class Solution(object):
    def __init__(self, n, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """

        self.n = n
        self.blacklist = set(blacklist)
        self.w = n - len(self.blacklist)
        self.whitelist = []

        if len(self.blacklist) * 1.0 / n > 0.25:
            for num in range(n):
                if num not in self.blacklist:
                    self.whitelist.append(num)

    def pick(self):
        """
        :rtype: int
        """

        if self.whitelist:
            return self.whitelist[randrange(0, self.w)]
        else:
            num = randrange(0, self.n)
            while num in self.blacklist:
                num = randrange(0, self.n)

            return num


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()