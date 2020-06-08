class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        result = []
        if not nums:
            return result

        prev = nums[0]
        string = ""

        for elem in nums[1:]:
            if elem != prev + 1:
                result.append(string + str(prev))
                string = ""
            elif not string:
                string += str(prev) + "->"

            prev = elem

        result.append(string + str(prev))
        return result