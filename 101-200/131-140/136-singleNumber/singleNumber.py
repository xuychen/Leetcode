import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        for num in nums:
            result ^= num

        return result

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return reduce(operator.__xor__, nums)