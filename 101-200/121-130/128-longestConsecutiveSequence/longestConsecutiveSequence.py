class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in nums:
                y = num + 1
                while y in nums:
                    y += 1

                best = max(best, y-num)

        return best

class Solution(object):
    def binary_search(self, alist, x, left, right):
        while left < right:
            mid = left + (right - left) / 2
            if alist[mid][0] == x[0]:
                return mid
            elif alist[mid][0] < x[0]:
                left = mid + 1
            else:
                right = mid

        return left

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        ranges = [[nums[0], nums[0]]]
        for num in nums[1:]:
            length = len(ranges)
            index = self.binary_search(ranges, [num, num], 0, length)
            if index == 0:
                if ranges[index][0] == num + 1:
                    ranges[index][0] = num
                elif num < ranges[0][0] - 1:
                    ranges.insert(0, [num, num])
            elif index == length:
                if ranges[index-1][1] == num - 1:
                    ranges[index-1][1] = num
                elif num > ranges[index-1][1] + 1:
                    ranges.append([num, num])
            else:
                if ranges[index-1][1] == num - 1 and ranges[index][0] == num + 1:
                    ranges[index-1][1] = ranges[index][1]
                    del ranges[index]
                elif ranges[index-1][1] == num - 1:
                    ranges[index-1][1] = num
                elif ranges[index][0] == num + 1:
                    ranges[index][0] = num
                elif ranges[index-1][1] + 1 < num < ranges[index][0] - 1:
                    ranges.insert(index, [num, num])

        maximum = 0
        for start, end in ranges:
            maximum = max(maximum, end-start+1)

        return maximum
            