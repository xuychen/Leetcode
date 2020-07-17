class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        length = len(nums)
        upcount = downcount = 1
        upvalue = downvalue = nums[0]

        for i in range(1, length):
            tmpup, tmpdown = upvalue, downvalue
            tmpupcount, tmpdowncount = upcount, downcount

            if nums[i] > tmpdown and tmpupcount <= tmpdowncount + 1:
                upcount = tmpdowncount + 1
                upvalue = nums[i]
            else:
                upvalue = max(upvalue, nums[i])

            if nums[i] < tmpup and tmpdowncount <= tmpupcount + 1:
                downcount = tmpupcount + 1
                downvalue = nums[i]
            else:
                downvalue = min(downvalue, nums[i])

        return max(upcount, downcount)