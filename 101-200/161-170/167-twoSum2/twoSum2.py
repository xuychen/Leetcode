class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        dictionary = {}
        for i in range(len(numbers)):
            if numbers[i] in dictionary:
                return [dictionary[numbers[i]], i+1]
            else:
                dictionary[target-numbers[i]] = i+1

        return []