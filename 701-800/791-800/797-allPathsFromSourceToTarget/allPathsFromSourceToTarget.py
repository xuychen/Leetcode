class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        return self.helper(graph, 0, len(graph) - 1)

    def helper(self, graph, node, end):
        if node == end:
            return [[end]]

        result = []
        for next_node in graph[node]:
            for elem in self.helper(graph, next_node, end):
                result.append([node] + elem)

        return result