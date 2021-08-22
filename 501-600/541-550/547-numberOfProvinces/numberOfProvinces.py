class UnionFind(object):
    def __init__(self):
        self.table = {}

    def union(self, x, y):
        self.table[self.find(x)] = self.find(y)

    def find(self, x):
        self.table.setdefault(x, x)
        return x if self.table[x] == x else self.find(self.table[x])


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        n = len(isConnected)
        uf = UnionFind()

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)

        count = set()
        for i in range(n):
            count.add(uf.find(i))

        return len(count)