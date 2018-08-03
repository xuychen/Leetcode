class Solution(object):
    def combinationSum2(self, candidates, target):
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
            
        result = []
        for i in range(startIndex, len(candidates)):
            num = candidates[i]
            if num > target:
                break
            if i == startIndex or candidates[i-1] != num:
                result += self.adding(candidates, i + 1, target - num, output + [num])
                
        return result