class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def DFS(i, j, pos):
            if board[i][j] == word[pos]:
                if pos == len(word) - 1:
                    return True
                
                board[i][j] = "#"
                if i != 0 and DFS(i-1, j, pos+1):
                    return True
                elif i != rows - 1 and DFS(i+1, j, pos+1):
                    return True
                elif j != 0 and DFS(i, j-1, pos+1):
                    return True
                elif j != cols - 1 and DFS(i, j+1, pos+1):
                    return True
            
                board[i][j] = word[pos]
            return False
        
        rows = len(board)
        
        if rows == 0:
            if word == "":
                return True
            else:
                return False
        else:
            cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if DFS(i, j, 0):
                    return True
                
        return False