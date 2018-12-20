class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        visited = {}
        
        xLength = len(board)
        yLength = xLength and len(board[0])
        
        for i in range(1, xLength-1):
            for j in range(1, yLength-1):
                if board[i][j] == 'O' and not visited.get((i,j), False):
                    path = {}
                    notFill = self.dfs(board, path, i, j, xLength, yLength)
                    if not notFill:
                        self.fillSpace(board, path)
                    else:
                        for key, value in path:
                            visited[key] = value
                
    def dfs(self, board, visited, i, j, xLength, yLength):
        if visited.get((i,j), False):
            return False
        if (i == 0 or j == 0 or i == xLength -1 or j == yLength - 1):
            return board[i][j] == 'O'
        
        if board[i][j] == 'O':
            visited[i,j] = True
            up = self.dfs(board, visited, i+1, j, xLength, yLength)
            down = self.dfs(board, visited, i-1, j, xLength, yLength)
            right = self.dfs(board, visited, i, j+1, xLength, yLength)
            left = self.dfs(board, visited, i, j-1, xLength, yLength)
            return up or down or right or left
        
        return False
    
    def fillSpace(self, board, path):
        for i, j in path:
            board[i][j] = 'X'