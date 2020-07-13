class Solution(object):
    # Newton
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        r = num
        while r * r > num:
            r = (r + num / r) / 2

        return r * r == num

    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """

        base = 1
        while base ** 2 < num:
            base += 1

        return base ** 2 == num