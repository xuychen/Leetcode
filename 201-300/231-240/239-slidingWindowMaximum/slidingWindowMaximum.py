import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()

            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dq = collections.deque()
        length = len(nums)
        result = []

        for i in range(k):
            while dq and dq[-1] < nums[i]:
                dq.pop()

            dq.append(nums[i])

        for i in range(k, length):
            result.append(dq[0])
            if nums[i-k] == dq[0]:
                dq.popleft()

            while dq and dq[-1] < nums[i]:
                dq.pop()

            dq.append(nums[i])

        result.append(dq[0])
        return result