class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """

        costs.sort()
        count = 0

        for cost in costs:
            if cost > coins:
                return count

            coins -= cost
            count += 1

        return count
