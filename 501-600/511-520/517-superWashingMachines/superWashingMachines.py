class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """

        length = len(machines)
        summation = sum(machines)
        if summation % length:
            return -1

        avg = summation / length
        result = 0
        s = 0

        for num in machines:
            num -= avg
            s += num
            result = max(num, abs(s), result)

        return result