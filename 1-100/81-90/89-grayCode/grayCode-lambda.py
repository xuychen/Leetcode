import itertools

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        return map(lambda x: x ^ x>>1, itertools.islice(itertools.count(), 1 << n))