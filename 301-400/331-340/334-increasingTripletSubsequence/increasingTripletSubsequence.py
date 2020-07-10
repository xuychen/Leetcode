import bisect 

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        result = []
        size = 0

        for num in nums:
            index = bisect.bisect_left(result, num)
            if index == size:
                size += 1
                result.append(num)
                if size == 3:
                    return True
            else:
                result[index] = num

        return False