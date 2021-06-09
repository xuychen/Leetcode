# a version that has O(n^2), too slow

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        less = filter(lambda x: x < 0, nums)
        greater = filter(lambda x: x > 0, nums)

        lessLen = len(less)
        greaterLen = len(greater)
        zeroLen = len(nums) - lessLen - greaterLen

        result = self.findingSum(greater+[0]*int(bool(zeroLen)), less)
        result += self.findingSum(less, greater)

        if zeroLen >= 3:
            result.append([0,0,0])
        return result

    # less means length is less
    # greater means length is longer
    def findingSum(self, less, greater):
        lessLen = len(less)
        greaterLen = len(greater)

        result = []

        dictionary = {}
        uniq = {}

        for num in greater:
            dictionary[-num] = True

        for i in range(lessLen):
            for j in range(i+1, lessLen):
                pair = (less[i], less[j]) if less[i] < less[j] else (less[j], less[i])
                if uniq.get(pair, False) == False:
                    uniq[pair] = True
                else:
                    continue

                if dictionary.get(less[i] + less[j], False) == True:
                    result.append([less[i], less[j], -less[i] - less[j]])

        return result

    def threeSum3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        nums_dict = {}
        result = set()
        length = len(nums)

        for i in range(length):
            nums_dict[nums[i]] = i

        for i in range(length):
            target = nums[i]
            for left in range(i+1, length-1):
                if -target-nums[left] in nums_dict and left < nums_dict[-target-nums[left]]:
                    result.add((target, nums[left], -target-nums[left]))

        return list(result)