class Solution(object):
    def __init__(self):
        self.dp = {}

    def findTargetSumWays(self, nums, S, index=0):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        if index == len(nums):
            return not S
        if (S, index) not in self.dp:
            self.dp[(S, index)] = sum([self.findTargetSumWays(nums, S + sign * nums[index], index + 1) for sign in (1, -1)])

        return self.dp[(S, index)]

    def findTargetSumWays2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        num_dict = {}
        num_dict[0] = 1

        for num in nums:
            new_dict = {}
            for key, value in num_dict.items():
                if key + num not in new_dict:
                    new_dict[key+num] = value
                else:
                    new_dict[key+num] += value

                if key - num not in new_dict:
                    new_dict[key-num] = value
                else:
                    new_dict[key-num] += value

            num_dict = new_dict

        return num_dict[target] if target in num_dict else 0