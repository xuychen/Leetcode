import sys

class UnionFind(object):
    def __init__(self, n):
        self.table = [-1] * n

    def union(self, x, y):
        self.table[self.find(x)] = self.find(y)

    def find(self, x):
        if self.table[x] == -1:
            self.table[x] = x

        return x if self.table[x] == x else self.find(self.table[x])

    def connected(self, x, y):
        return self.find(x) == self.find(y)

n, m = map(int, sys.stdin.readline().strip().split())
edges = []

for _ in range(m):
    start, end, score = map(int, sys.stdin.readline().strip().split())
    edges.append((score, start-1, end-1))

edges.sort(key=lambda x: -x[0])
uf = UnionFind(n)
scores = 0

for score, start, end in edges:
    if not uf.connected(start, end):
        uf.union(start, end)
        scores += score

for mark in uf.table:
    if mark == -1:
        print("No solution.")
        break

if mark != -1:
    print(scores)