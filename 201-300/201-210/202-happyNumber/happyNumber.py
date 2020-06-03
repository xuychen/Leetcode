class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        visited = set()
        visited.add(n)

        while n != 1:
            n, num = 0, n
            while num > 0:
                n += (num % 10) ** 2
                num /= 10

            if n in visited:
                return False
            else:
                visited.add(n)

        return True
    