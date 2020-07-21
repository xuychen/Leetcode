class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.original = nums
        self.array = nums[:]


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """

        self.array = self.original[:]
        return self.array

    def shuffle2(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        random.shuffle(self.array)
        return self.array

    # Knuth-Durstenfeld Shuffle
    def shuffle(self):
        for i in range(len(self.array)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index
            self.array[i], self.array[j] = self.array[j], self.array[i]    # swap

        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()