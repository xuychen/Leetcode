import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        ctr = collections.Counter(s)
        ctr.subtract(t)
        return not any(ctr.values())