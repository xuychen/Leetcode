# adding type dp with sort and breaking
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        array = [[[]]] + [[] for i in range(target)]
        dictionary = {}        
        
        for i, num in enumerate(candidates):
            dictionary[num] = i
        
        length = i + 1
        for i in range(0, target+1):
            for elem in array[i]:
                startIndex = dictionary[elem[-1]] if elem else 0
                for j in range(startIndex, length):
                    num = candidates[j]
                    if num + i > target:
                        break
                    else:
                        array[num+i].append(elem+[num])
                        
        return array[-1]