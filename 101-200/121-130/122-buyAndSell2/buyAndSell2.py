class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        if length == 0:
            return 0

        result = 0
        buy = prices[0]
        sell = 0

        for i in range(1, length):
            if sell == 0:
                diff = prices[i] - buy
                if diff <= 0:
                    buy = prices[i]
                else:
                    sell = prices[i]
            else:
                diff = prices[i] - sell
                if diff >= 0:
                    sell = prices[i]
                else:
                    result += sell - buy
                    buy = prices[i]
                    sell = 0

        if prices[length-1] >= prices[length-2]:
            sell = prices[length-1]
            result += sell - buy

        return result
        
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        prices.append(float('-inf'))
        profit = 0
        min_price = float('inf')
        prev_price = float('inf')

        for price in prices:
            if price < prev_price:
                difference = prev_price - min_price
                profit += difference if difference > 0 else 0
                min_price = price

            prev_price = price

        return profit