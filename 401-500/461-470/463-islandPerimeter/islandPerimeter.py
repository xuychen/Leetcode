import Queue

class Solution(object):
    def find_island(self, grid, rows, cols):
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return i, j

    def move(self, grid, pos, rows, cols):
        result = []
        i, j = pos
        if i and grid[i-1][j]:
            result.append((i-1, j))
        if i < rows-1 and grid[i+1][j]:
            result.append((i+1, j))
        if j and grid[i][j-1]:
            result.append((i, j-1))
        if j < cols-1 and grid[i][j+1]:
            result.append((i, j+1))

        return result


    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows = len(grid)
        cols = len(grid[0])

        qe = Queue.Queue(maxsize=0)
        visited = set()
        qe.put(self.find_island(grid, rows, cols))
        count = 0

        while not qe.empty():
            pos = qe.get()
            if pos not in visited:
                visited.add(pos)
                next_move = self.move(grid, pos, rows, cols)
                count += 4 - len(next_move)
                for next_pos in next_move:
                    qe.put(next_pos)

        return count

    # amazing solution from others
    def islandPerimeter(self, grid):
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
                for row in grid + map(list, zip(*grid)))