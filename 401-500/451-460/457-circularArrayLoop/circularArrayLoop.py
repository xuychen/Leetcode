class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        length = len(nums)
        visited = set()

        for i in range(length):
            new_visited = set()
            prev = i - 1
            direction = (-1, 1)[nums[i] > 0]
            while i not in visited and i != prev and nums[i] * direction > 0:
                if i in new_visited:
                    return True

                new_visited.add(i)
                prev, i = i, (nums[i] + i) % length

            visited |= new_visited

        return False
        