class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):
            dist_old = dist[:]
            for u, v, w in flights:
                dist[v] = min(dist[v], dist_old[u] + w)

        return dist[dst] if dist[dst] != float('inf') else -1