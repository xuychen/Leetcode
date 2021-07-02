import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        n_rows = len(matrix)
        n_cols = len(matrix[0])
        array = []
        heapq.heappush(array, (matrix[0][0], 0, 0))
        count = 0

        while array and count < k:
            value, x, y = heapq.heappop(array)
            if y < n_cols - 1:
                heapq.heappush(array, (matrix[x][y+1], x, y+1))
            if y == 0 and x < n_rows - 1:
                heapq.heappush(array, (matrix[x+1][y], x+1, y))

            count += 1

        return value