import Queue

class Solution(object):
    def numWays(self, n, relation, k):
        """
        :type n: int
        :type relation: List[List[int]]
        :type k: int
        :rtype: int
        """

        graph = [[] for _ in range(n)]
        qe = Queue.Queue(maxsize=0)
        node, level = 0, 0
        qe.put((node, level))

        for start, end in relation:
            graph[start].append(end)

        while not qe.empty() and level < k:
            node, level = qe.get()
            if level != k:
                for next_node in graph[node]:
                    qe.put((next_node, level+1))

        count = int(node == n - 1 and level == k)
        while not qe.empty():
            count += qe.get()[0] == n - 1

        return count