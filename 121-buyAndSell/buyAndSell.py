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