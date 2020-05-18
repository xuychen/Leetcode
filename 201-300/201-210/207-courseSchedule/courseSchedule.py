import Queue

class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adjacency_list = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        qe = Queue.Queue(maxsize=0)

        for edge in prerequisites:
            start, end = edge[1], edge[0]
            adjacency_list[start].append(end)
            degrees[end] += 1

        for vertex in range(numCourses):
            if degrees[vertex] == 0:
                qe.put(vertex)

        while not qe.empty():
            for elem in adjacency_list[qe.get()]:
                degrees[elem] -= 1
                if degrees[elem] == 0:
                    qe.put(elem)

        return sum(degrees) == 0