class Solution(object):
    def mergesort(self, nums):
        length = len(nums)
        if length <= 1:
            return nums, 0

        left_nums, left_value = self.mergesort(nums[:length/2])
        right_nums, right_value = self.mergesort(nums[length/2:])
        left_length, right_length = length/2, length-length/2
        new_nums = []

        i, j = 0, 0
        counter = 0

        while i < left_length and j < right_length:
            if left_nums[i] > right_nums[j]:
                new_nums.append(right_nums[j])
                j += 1
            else:
                new_nums.append(left_nums[i])
                counter += j
                i += 1

        if i == left_length:
            new_nums += right_nums[j:]
        else:
            new_nums += left_nums[i:]
            counter += j * (left_length - i)

        return new_nums, left_value + right_value + counter

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.mergesort(nums)[1]