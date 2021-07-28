class Solution(object):
    def __init__(self):
        self.memory = {}
    
    def trace(self, graph, x, mask):
        if not mask:
            return 0
        if (x, mask) in self.memory:
            return self.memory[(x, mask)]
        
        answer = float('inf')
        for i in range(len(graph)):
            if mask & (1 << i):
                answer = min(answer, self.trace(graph, i, mask ^ (1 << i)) + graph[x][i])
                
        self.memory[(x, mask)] = answer
        return answer
    
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        
        length = len(graph)
        adj = [[float('inf')] * length for _ in range(length)]
        result = float('inf')
        
        for i in range(length):
            adj[i][i] = 0
            for elem in graph[i]:
                adj[i][elem] = 1
        
        for k in range(length):
            for i in range(length):
                for j in range(length):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
                    
        
        mask = (1 << length) - 1
        for i in range(length):
            result = min(result, self.trace(adj, i, mask))
            
        return result