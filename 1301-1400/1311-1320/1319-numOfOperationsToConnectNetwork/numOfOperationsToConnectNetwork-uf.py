class UnionFind(object):
    def __init__(self):
        self.table = {}

    def find(self, x):
        self.table.setdefault(x, x)
        return x if self.table[x] == x else self.find(self.table[x])

    def union(self, x, y):
        self.table[self.find(x)] = self.find(y)

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        uf = UnionFind()
        size = len(connections)
        count = 0
        if size < n - 1:
            return -1

        for start, end in connections:
            if uf.find(start) == uf.find(end):
                count += 1
            else:
                uf.union(start, end)

        return count - (size - n + 1)