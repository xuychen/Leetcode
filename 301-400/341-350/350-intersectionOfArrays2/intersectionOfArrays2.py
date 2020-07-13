from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        counter = Counter(nums1)
        result = []

        for num in nums2:
            if counter.get(num, 0):
                result.append(num)
                counter[num] -= 1

        return result