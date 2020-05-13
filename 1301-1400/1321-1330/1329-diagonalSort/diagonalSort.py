import collections

class Solution(object):
    def diagonalRead(self, mat):
        x_len, y_len = len(mat), len(mat[0])
        arrays = [[] for _ in range(x_len + y_len - 1)]

        for i in range(x_len):
            for j in range(y_len):
                arrays[x_len-i-1+j].append(mat[i][j])

        return arrays

    def diagonalWrite(self, arrays, x_len):
        arrays_len = len(arrays)
        y_len = arrays_len + 1 - x_len
        mat = [[0] * y_len for _ in range(x_len)]

        for i in range(x_len):
            x, y = i, 0
            array = arrays[x_len-1-i]

            for elem in array:
                mat[x][y] = elem
                x, y = x + 1, y + 1

        for i in range(1, y_len):
            x, y = 0, i
            array = arrays[x_len-1+i]

            for elem in array:
                mat[x][y] = elem
                x, y = x + 1, y + 1

        return mat

    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        arrays = self.diagonalRead(mat)
        for array in arrays:
            array.sort()

        return self.diagonalWrite(arrays, len(mat))

    # good alternative solution from others
    def diagonalSort2(self, A):
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)
        for i in xrange(n):
            for j in xrange(m):
                d[i - j].append(A[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in xrange(n):
            for j in xrange(m):
                A[i][j] = d[i - j].pop()
        return A