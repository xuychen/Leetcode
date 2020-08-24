from collections import defaultdict

class UnionFind(object):
    def __init__(self):
        self.table = {}
        self.values = defaultdict(dict)
        
    def merge(self, x, y, value):
        self.values[x][x] = self.values[y][y] = 1
        left, right = self.find(x), self.find(y)
        self.values[left][right] = value * self.findvalue(y)[0] / self.findvalue(x)[0]
        self.table[left] = right
        
    def find(self, x):
        if x not in self.table:
            self.table[x] = x
            
        return x if self.table[x] == x else self.find(self.table[x])
    
    def findvalue(self, x):
        value = 1
        while x in self.table and self.table[x] != x:
            value *= self.values[x][self.table[x]]
            x = self.table[x]
            
        return value, x
    
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        uf = UnionFind()
        result = []
        
        for equation, value in zip(equations, values):
            uf.merge(equation[0], equation[1], value)
            
        for start, end in queries:
            if start in uf.table and start == end:
                result.append(1)
            else:
                left = uf.findvalue(start)
                right = uf.findvalue(end)
                result.append(-1 if start not in uf.table or left[1] != right[1] else left[0] / right[0])
                
        return result