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

# detect Cycle ver.
class Solution2(object):
    def detectCycle(self, graph, start, node, visited):
        visited.add(node)
        for next_node in graph[node]:
            if next_node == start:
                return False
            if next_node not in visited and not self.detectCycle(graph, start, next_node, visited):
                return False

        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = [[] for _ in range(numCourses)]
        for node1, node2 in prerequisites:
            graph[node1].append(node2)

        for start in range(numCourses):
            visited = set()
            if not self.detectCycle(graph, start, start, visited):
                return False

        return True