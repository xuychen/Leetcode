class Solution(object):
    def minSwap(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        length = len(nums1)
        dp_change = [float('inf')] * length
        dp_nochange = [float('inf')] * length
        dp_change[0] = 1
        dp_nochange[0] = 0

        for i in range(1, len(nums1)):
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                dp_change[i] = dp_nochange[i-1] + 1
                dp_nochange[i] = dp_change[i-1]
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                dp_change[i] = min(dp_change[i-1] + 1, dp_change[i])
                dp_nochange[i] = min(dp_nochange[i-1], dp_nochange[i])

        return min(dp_change[-1], dp_nochange[-1])