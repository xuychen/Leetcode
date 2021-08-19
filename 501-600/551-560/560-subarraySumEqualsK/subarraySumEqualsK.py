from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        length = len(nums)
        summations = [0] * (length+1)
        counter = defaultdict(int)
        count = 0

        for i in range(1, length+1):
            summations[i] += summations[i-1] + nums[i-1]

        counter[0] = 1
        for i in range(1, length+1):
            if summations[i] - k in counter:
                count += counter[summations[i]-k]

            counter[summations[i]] += 1

        return count