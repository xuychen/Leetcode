import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        visited = [False] * n
        count = n
        adj = [{} for _ in range(n)]
        array = []

        for start, end, weight in times:
            adj[start-1][end-1] = weight

        heapq.heappush(array, (0, k-1))

        while array and count > 0:
            time, node = heapq.heappop(array)
            if not visited[node]:
                visited[node] = True
                count -= 1

            for next_node, weight in adj[node].items():
                if not visited[next_node]:
                    heapq.heappush(array, (time+weight, next_node))

        return time if count == 0 else -1