from collections import defaultdict, Counter

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = defaultdict(int)
        dp[(0, 0)] = 0
        result = 0
        
        for string in strs:
            counter = Counter(string)
            x, y = counter['0'], counter['1']
            newdp = dp.copy()
            for i, j in dp.keys():
                if i + x <= m and j + y <= n:
                    newdp[(i+x, j+y)] = max(newdp[(i+x, j+y)], dp[(i,j)] + 1)
                    result = max(result, newdp[(i+x, j+y)])
                    
            dp = newdp        
        return result