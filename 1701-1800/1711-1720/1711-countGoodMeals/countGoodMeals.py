from collections import defaultdict

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """

        max_sum = max(deliciousness) * 2
        count = 0
        dictionary = defaultdict(int)

        for value in deliciousness:
            summation = 1
            while summation <= max_sum:
                count = (count + dictionary[summation-value]) % 1000000007
                summation <<= 1

            dictionary[value] += 1

        return count
