class UnionFind(object):
    def __init__(self):
        self.table = {}

    def union(self, x, y):
        self.table[self.find(x)] = self.find(y)

    def find(self, x):
        self.table.setdefault(x, x)
        return x if self.table[x] == x else self.find(self.table[x])

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        uf = UnionFind()
        result = None

        for edge in edges:
            x, y = edge
            if uf.find(x) != uf.find(y):
                uf.union(x, y)
            elif not result:
                result = edge
            else:
                result = edges[-1]
                break

        return result
