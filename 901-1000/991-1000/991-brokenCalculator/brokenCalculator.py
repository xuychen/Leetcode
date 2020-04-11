class Solution:
    def brokenCalc(self, x, y):
        result = 0
        while x < y:
            result += (y & 1) + 1
            y = (y + 1) // 2

        return x - y + result