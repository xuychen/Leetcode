from collections import Counter

class UnionFind(object):
    def __init__(self):
        self.table = {}

    def merge(self, v1, v2):
        self.table[self.find(v1)] = self.find(v2)

    def find(self, v1):
        if v1 not in self.table:
            self.table[v1] = v1

        return v1 if self.table[v1] == v1 else self.find(self.table[v1])

def largest_item_association(items):
    uf = UnionFind()
    for v1, v2 in items:
        uf.merge(v1, v2)

    return max(Counter(map(lambda x: uf.find(x), uf.table.keys())).values())

items1 = [["Item1", "Item2"],
["Item3", "Item4"],
["Item4", "Item5"]]

items2 = [["item3","item4"],
["item1","item2"],
["item5","item6"],
["item4","item5"],
["item2","item7"],
["item7","item8"],
["item2","item3"],
["item6","item7"],
["item0","item2"]]

print (largest_item_association(items1)) # 3
print (largest_item_association(items2)) # 9

print(largest_item_association([['A', 'B'], ['D', 'E'], ['C', 'D']]) == 3)
print(largest_item_association([['A', 'B'], ['C', 'D'], ['F', 'E']]) == 2)
print(largest_item_association([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]) == 4)
print(largest_item_association([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]) == 6)
print(largest_item_association([['A', 'B'], ['F', 'E'], ['G', 'K'], ['C', 'D'], ['D', 'E'],
            ['X', 'G'], ['X', 'N'], ['K', 'L'], ['L', 'M'], ['F', 'E'],
            ['A', 'C'],]) == 6)
print(largest_item_association([['item1','item2'],['item3','item4'],['item4','item5']]) == 3)
print(largest_item_association([['item1','item2'],['item2','item5'],['item3', 'item6']]) == 3)
print(largest_item_association([['item1','item2'],['item2','item3'],['item4','item5'],['item5','item6']]) == 3)
print(largest_item_association([["item1","item2"], ["item1","item3"], ["item2","item7"], ["item3","item7"], ["item5","item6"], ["item3","item7"]]) == 4)

print(largest_item_association([['item1', 'item2'], ['item1', 'item4'], ['item3', 'item4'], ['item4', 'item5']]) == 5)

print(largest_item_association([["item3","item4"], ["item1","item2"], ["item5","item6"], ["item4","item5"], ["item2","item7"], ["item7","item8"]]) == 4)

print(largest_item_association([["item1","item2"], ["item3","item4"], ["item5","item6"], ["item4","item5"]]) == 4)