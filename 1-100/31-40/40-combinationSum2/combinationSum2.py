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

class Solution2(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        return self.helper(sorted(candidates), target)

    def helper(self, candidates, target):
        if target == 0:
            return [[]]
        if not candidates:
            return []

        result = []
        prev = float('-inf')
        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate > target:
                break
            if prev != candidate:
                rhs = self.combinationSum2(candidates[i+1:], target-candidate)
                for element in rhs:
                    result.append([candidate]+element)

            prev = candidate
        return result