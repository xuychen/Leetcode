import bisect

class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """

        sum_chalks = chalk[:]
        for i in range(1, len(chalk)):
            sum_chalks[i] += sum_chalks[i-1]

        return bisect.bisect(sum_chalks, k % sum_chalks[-1])