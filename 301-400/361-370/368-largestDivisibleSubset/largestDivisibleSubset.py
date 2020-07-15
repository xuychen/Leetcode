class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        length = len(nums)
        prev, count = [-1] * length, [1] * length
        result = []

        for end in range(1, length):
            maximum = 0
            i = -1
            for index in range(end):
                if not nums[end] % nums[index]:
                    if maximum < count[index]:
                        maximum = count[index]
                        i = index

            if maximum:
                count[end] += maximum
                prev[end] = i

        maximum = 0
        index = -1
        for i, num in enumerate(count):
            if maximum < num:
                maximum, index = num, i

        while index != -1:
            result.append(nums[index])
            index = prev[index]

        return result[::-1]