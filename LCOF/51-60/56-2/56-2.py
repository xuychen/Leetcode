class Solution:
    # two good answer from discussion.
    def singleNumber(self, nums):
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1

        result, m = 0, 3
        for i in range(32):
            result <<= 1
            result |= counts[31-i] % m

        return result

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ones = twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones