class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        k %= length

        if k != 0:
            nums.extend(nums[:-k])
            del nums[:length-k]

class Solution2(object):
    def gcd(self, num1, num2):
        while num2:
            remainder = num1 % num2
            num1, num2 = num2, remainder

        return num1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        k %= length

        if k == 0:
            return

        rounds = self.gcd(length, k)
        offset = length % rounds
        steps = length / rounds

        for i in range(rounds):
            index = i
            tmp = nums[index]
            for j in range(steps + (i < offset)):
                next_index = (index + k) % length
                tmp, nums[next_index] = nums[next_index], tmp
                index = next_index
