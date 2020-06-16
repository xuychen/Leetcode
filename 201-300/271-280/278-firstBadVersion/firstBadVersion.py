# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    # an imaginary definition of isBadVersion function to remove error
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        first, last = 0, n

        while first < last:
            mid = (first + last) / 2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1

        return first