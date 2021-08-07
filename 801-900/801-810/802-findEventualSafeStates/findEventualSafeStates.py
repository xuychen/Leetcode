from collections import deque

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        length = len(graph)
        inv_graph = [[] for _ in range(length)]
        degrees = [0] * length
        result = []
        dq = deque()

        for i in range(length):
            for j in graph[i]:
                inv_graph[j].append(i)
                degrees[i] += 1

        for i in range(length):
            if degrees[i] == 0:
                dq.append(i)

        while dq:
            node = dq.popleft()
            for next_node in inv_graph[node]:
                degrees[next_node] -= 1
                if degrees[next_node] == 0:
                    dq.append(next_node)

        for i in range(length):
            if degrees[i] == 0:
                result.append(i)

        return result
