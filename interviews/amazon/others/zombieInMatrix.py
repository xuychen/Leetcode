def dfs(grid, i, j, rows, cols, visited, steps=set()):
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return float('inf')
    if grid[i][j] == 1:
        return 0
    if visited[i][j] != -1:
        return visited[i][j]

    steps.add((i, j))
    visited[i][j] = min([dfs(grid, i+x, j+y, rows, cols, visited) for x, y in [(0, 1), (0, -1), (1, 0), (-1,0)] if (i+x, j+y) not in steps]) + 1
    steps.remove((i, j))
    return visited[i][j]


def minHour(grid):
    if not grid:
        return False

    rows = len(grid)
    cols = len(grid[0])

    visited = [[-1] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            visited[i][j] = dfs(grid, i, j, rows, cols, visited)

    return max(map(max, visited))

# good bfs solution
def minHour(self, rows, columns, grid):
    if not rows or not columns:
        return 0

    q = [[i,j] for i in range(rows) for j in range(columns) if grid[i][j]==1]
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    time = 0

    while True:
        new = []
        for [i,j] in q:
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    new.append([ni,nj])

        q = new
        if not q:
            break
        time += 1

    return time

input = [[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,1]]
# [[0, 1, 1, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]

print(minHour(input))