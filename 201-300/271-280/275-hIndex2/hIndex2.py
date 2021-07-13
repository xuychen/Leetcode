class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        length = len(citations)
        left, right = 0, length

        while left < right:
            mid = left + (right - left) / 2
            if citations[mid] < length - mid:
                left = mid + 1
            else:
                right = mid

        return length - left