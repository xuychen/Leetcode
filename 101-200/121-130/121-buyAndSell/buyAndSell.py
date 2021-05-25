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
                    if result < sell - buy:
                        result = sell - buy
                    if buy > prices[i]:
                        buy = prices[i]
                    sell = 0

        if prices[length-1] > prices[length-2]:
            sell = prices[length-1]
            if result < sell - buy:
                result = sell - buy

        return result

    # max version
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        length = len(prices)
        max_array = prices[:]

        for i in range(length-2, -1, -1):
            max_array[i] = max(prices[i], max_array[i+1])

        max_value = 0
        for i in range(length-1):
            max_value = max(max_value, max_array[i+1] - prices[i])

        return max_value

    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price-min_price)

        return max_profit
