class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        waves = [0] * (n + 1)
        result = [0] * n

        for start, end, value in bookings:
            waves[start-1] += value
            waves[end] -= value

        summation = 0
        for i in range(n):
            summation += waves[i]
            result[i] = summation

        return result