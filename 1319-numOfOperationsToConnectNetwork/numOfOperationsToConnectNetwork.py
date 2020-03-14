# "Union Find" Solution from others
# small range, for n <= 256
def makeConnected(self, n, connections):
    if len(connections) < n - 1:
        return -1
    s = ''.join(map(chr, range(n)))
    for a, b in connections:
        s = s.replace(s[a], s[b])
    return len(set(s)) - 1

# general ver. 
def makeConnected2(self, n, connections):
    if len(connections) < n - 1: return -1
    G = [set() for i in xrange(n)]
    for i, j in connections:
        G[i].add(j)
        G[j].add(i)
    seen = [0] * n

    def dfs(i):
        if seen[i]: return 0
        seen[i] = 1
        for j in G[i]: dfs(j)
        return 1

    return sum(dfs(i) for i in xrange(n)) - 1