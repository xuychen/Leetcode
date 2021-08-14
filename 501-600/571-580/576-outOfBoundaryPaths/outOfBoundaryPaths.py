from collections import defaultdict, deque

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """

        dq = deque()
        dq.append((startRow, startColumn, 1))

        result = 0
        MOD = 10**9 + 7
        operations = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for _ in range(maxMove):
            next_steps = defaultdict(int)
            while dq:
                x, y, count = dq.popleft()
                for xx, yx in operations:
                    if x + xx < 0 or y + yx < 0 or x + xx >= m or y + yx >= n:
                        result = (result + count) % MOD
                    else:
                        next_steps[(x+xx, y+yx)] += count

            for key, value in next_steps.items():
                x, y = key
                dq.append((x, y, value % MOD))

        return int(result)