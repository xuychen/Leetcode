class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        nums = [1]
        c2 = c3 = c5 = 0
        count = 1

        while count < n:
            next_num = min(2*nums[c2], 3*nums[c3], 5*nums[c5])
            nums.append(next_num)

            if next_num == 2 * nums[c2]:
                c2 += 1
            if next_num == 3 * nums[c3]:
                c3 += 1
            if next_num == 5 * nums[c5]:
                c5 += 1

            count += 1

        return nums[-1]