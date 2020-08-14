class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """

        if target > d * f or target < d:
            return 0

        result = [0] * (target + 1)
        for last in range(1, min(target,f)+1):
            result[last] = 1

        for k in range(1, d):
            new_result = [0] * (target + 1)
            for i in range(k, last+1):
                for j in range(1, min(f, target-i)+1):
                    new_result[i+j] = int((new_result[i+j] + result[i]) % (1e9 + 7))

            result = new_result
            last += f

        return result[target]