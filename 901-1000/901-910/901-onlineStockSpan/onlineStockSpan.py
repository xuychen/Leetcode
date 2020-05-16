class StockSpanner(object):
    def __init__(self):
        self.next_table = []
        self.next_table.append((float('inf'), 1))

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        days = 1
        prev_index = len(self.next_table) - 1
        while price >= self.next_table[prev_index][0]:
            days += self.next_table[prev_index][1]
            prev_index -= self.next_table[prev_index][1]

        self.next_table.append((price, days))
        return days

# refined ver. of my answer
class StockSpanner2(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)