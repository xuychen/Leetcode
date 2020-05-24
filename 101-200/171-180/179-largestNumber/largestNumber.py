class Solution(object):
    def comparator(self, lhs, rhs):
        return cmp(lhs + rhs, rhs + lhs)

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        str_nums = sorted(map(str, nums), self.comparator, reverse=True)
        return "".join(str_nums) if str_nums[0] != "0" else "0"