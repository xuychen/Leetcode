import bisect

class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """

        index_array = []
        stock = []
        stock_index = 0
        num2index = {}

        for i, num in enumerate(target):
            num2index[num] = i

        for num in arr:
            if num in num2index:
                index_array.append(num2index[num])

        for num in index_array:
            index = bisect.bisect_left(stock, num)
            if index == stock_index:
                stock.append(num)
                stock_index += 1
            else:
                stock[index] = num

        return len(target) - stock_index
