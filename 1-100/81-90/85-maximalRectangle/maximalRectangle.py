import heapq

class UnionFind(object):
    def __init__(self):
        self.hashtable = {}
        self.sizes = {}

    def union(self, x, y):
        self.sizes.setdefault(self.find(y), 1)
        self.sizes[self.find(y)] += self.sizes.get(self.find(x), 1)
        self.hashtable[self.find(x)] = self.find(y)

    def find(self, x):
        self.hashtable.setdefault(x, x)
        return x if self.hashtable[x] == x else self.find(self.hashtable[x])

    def get_size(self, x):
        return self.sizes[self.find(x)]

# solution with UnionFind
class Solution(object):
    def find_maxarea(self, array, size):
        heap = zip(map(lambda x: -x, array), range(size))
        uf = UnionFind()
        heapq.heapify(heap)
        visited = set()
        mintable = {}
        result = 0

        while heap:
            height, index = heapq.heappop(heap)
            result = max(result, -height)

            for step in (-1, 1):
                if index + step in visited:
                    uf.union(index, index+step)
                    mintable.setdefault(uf.find(index), -height)
                    mintable[uf.find(index)] = min(mintable[uf.find(index)], -height, array[index+step])
                    result = max(result, uf.get_size(index) * mintable[uf.find(index)])

            visited.add(index)

        return result

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        n_rows = len(matrix)
        n_cols = n_rows and len(matrix[0])

        if not n_rows or not n_cols:
            return 0

        dp = [0] * n_cols

        for j in range(n_cols):
            dp[j] = int(matrix[0][j])

        result = self.find_maxarea(dp, n_cols)
        for i in range(1, n_rows):
            for j in range(n_cols):
                dp[j] = (dp[j] + 1) * int(matrix[i][j])

            result = max(result, self.find_maxarea(dp, n_cols))

        return result

# solution with monotonous stack
class Solution2(object):
    def find_min(self, heights, left):
        length = len(heights)

        if left:
            stack = [-1]
            sequence = range(length)
        else:
            stack = [length]
            sequence = range(length-1, -1, -1)

        mins = [0] * length
        stack_length = 1

        for i in sequence:
            while stack_length > 1 and heights[stack[-1]] >= heights[i]:
                stack.pop()
                stack_length -= 1

            stack.append(i)
            stack_length += 1
            mins[i] = stack[-2]

        return mins

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        left_min = self.find_min(heights, left=True)
        right_min = self.find_min(heights, left=False)
        max_area = 0

        for i in range(len(left_min)):
            max_area = max(max_area, (right_min[i] - left_min[i] - 1) * heights[i])

        return max_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        n_rows = len(matrix)
        n_cols = n_rows and len(matrix[0])

        if not n_rows or not n_cols:
            return 0

        dp = [0] * n_cols

        for j in range(n_cols):
            dp[j] = int(matrix[0][j])

        result = self.largestRectangleArea(dp)
        for i in range(1, n_rows):
            for j in range(n_cols):
                dp[j] = (dp[j] + 1) * int(matrix[i][j])

            result = max(result, self.largestRectangleArea(dp))

        return result