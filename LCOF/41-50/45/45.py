class Solution(object):
    def comparator(self, lhs, rhs):
        return cmp(lhs+rhs, rhs+lhs)

    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        return "".join(sorted(map(str, nums), self.comparator))