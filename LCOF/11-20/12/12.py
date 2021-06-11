class Solution(object):
    def dfs(self, board, n_rows, n_cols, i, j, word, depth):
        if not depth:
            return True
        if i < 0 or i >= n_rows or j < 0 or j >= n_cols or word[-depth] != board[i][j]:
            return False

        board[i][j] = ''
        result = self.dfs(board, n_rows, n_cols, i-1, j, word, depth-1) \
                    or self.dfs(board, n_rows, n_cols, i+1, j, word, depth-1) \
                    or self.dfs(board, n_rows, n_cols, i, j-1, word, depth-1) \
                    or self.dfs(board, n_rows, n_cols, i, j+1, word, depth-1)
        board[i][j] = word[-depth]
        return result

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board or not board[0]:
            return False

        n_rows, n_cols = len(board), len(board[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if self.dfs(board, n_rows, n_cols, i, j, word, len(word)):
                    return True

        return False