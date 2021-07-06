from collections import defaultdict

class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """

        dish_orders = defaultdict(lambda: defaultdict(int))
        dish_set = set()
        result = []

        for _, num, dish in orders:
            dish_orders[num][dish] += 1
            dish_set.add(dish)

        dish_list = sorted(list(dish_set))
        result.append(["Table"] + dish_list)
        for key, order in sorted(dish_orders.items(), key=lambda x: int(x[0])):
            dishes = [str(key)]
            for i in range(len(dish_list)):
                dishes.append(str(order[dish_list[i]]))

            result.append(dishes)

        return result
