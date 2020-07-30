class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        counter = Counter(s)
        nums = [0] * 10
        nums[0] = counter['z']
        nums[2] = counter['w']
        nums[4] = counter['u']
        nums[6] = counter['x']
        nums[8] = counter['g']

        nums[1] = counter['o'] - nums[0] - nums[2] - nums[4]
        nums[3] = counter['h'] - nums[8]
        nums[7] = counter['s'] - nums[6]
        nums[5] = counter['v'] - nums[7]
        nums[9] = counter['i'] - nums[5] - nums[6] - nums[8]

        return reduce(lambda a, b: a + b[1] * str(b[0]), enumerate(nums), '')