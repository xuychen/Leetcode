# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        if node.val not in self.visited:
            new_node = Node(node.val, [])
            self.visited[node.val] = new_node
            for neighbor in node.neighbors:
                new_neighbor = self.cloneGraph(neighbor)
                new_node.neighbors.append(new_neighbor)

        return self.visited[node.val]