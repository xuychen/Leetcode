import collections
import itertools

class Solution(object):
    def fourSumCount(self, A, B, C, D, depth=4, summation=0):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        summation1 = collections.Counter(map(sum, itertools.product(A, B)))
        summation2 = collections.Counter(map(lambda x: -x[0]-x[1], itertools.product(C, D)))
        return sum([summation1[key] * summation2[key] for key in summation1])

    def fourSumCount2(self, A, B, C, D):
        counter = collections.Counter(a+b for a in A for b in B)
        return sum(counter[-c-d] for c in C for d in D)