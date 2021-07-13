import bisect

class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        sorted_nums1 = sorted(nums1)
        length = len(nums1)
        largest = 0
        summation = 0
        MOD = 10**9 + 7

        for i in range(length):
            num = nums2[i]
            index = bisect.bisect(sorted_nums1, num)
            minimum = min(abs(nums2[i]-sorted_nums1[index-1]), abs(nums2[i]-sorted_nums1[index]) if index != length else float('inf'))
            original = abs(nums2[i]-nums1[i])
            summation += original
            largest = max(largest, original - minimum)

        return (summation - largest) % MOD