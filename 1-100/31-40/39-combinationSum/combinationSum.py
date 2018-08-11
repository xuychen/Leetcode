class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        return self.adding(candidates, 0, target, [])
        
    def adding(self, candidates, startIndex, target, output):
        if target == 0: 
            return [output]
        if target < candidates[startIndex]:
            return []
            
        result = []
        for i in range(startIndex, len(candidates)):
            num = candidates[i]
            result += self.adding(candidates, i, target - num, output + [num])
        
        return result