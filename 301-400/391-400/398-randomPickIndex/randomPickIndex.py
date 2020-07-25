class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.map = defaultdict(list)
        for i, num in enumerate(nums):
            self.map[num].append(i)


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        array = self.map[target]
        return array[random.randrange(len(array))]



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)