class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        sorted_range = sorted(ranges)
        length = len(ranges)
        index = 0
        start = left

        while start <= right and index < length:
            if start < sorted_range[index][0]:
                return False
            else:
                start = max(start, sorted_range[index][1] + 1)
                index += 1

        return start > right