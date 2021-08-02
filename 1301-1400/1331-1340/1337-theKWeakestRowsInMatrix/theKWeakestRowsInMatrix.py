class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        return map(lambda x: x[0], sorted(enumerate(mat), key=lambda x: ((sum(x[1]), x[0])))[:k])