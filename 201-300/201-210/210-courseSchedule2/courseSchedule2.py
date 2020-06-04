import Queue
import collections

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adjacency_list = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        result = []
        qe = Queue.Queue(maxsize=0)

        for edge in prerequisites:
            start, end = edge[1], edge[0]
            adjacency_list[start].append(end)
            degrees[end] += 1

        for vertex in range(numCourses):
            if degrees[vertex] == 0:
                qe.put(vertex)
                result.append(vertex)

        while not qe.empty():
            for elem in adjacency_list[qe.get()]:
                degrees[elem] -= 1
                if degrees[elem] == 0:
                    qe.put(elem)
                    result.append(elem)

        return result if sum(degrees) == 0 else []

    # BFS Solution from others
    def findOrder2(self, numCourses, prerequisites):
        dic = {i: set() for i in xrange(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []