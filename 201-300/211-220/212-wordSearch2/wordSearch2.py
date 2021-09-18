class Solution(object):
    def dfs(self, i, j, n_rows, n_cols, word, index, board):
        if index == -1:
            return True
        if i < 0 or i >= n_rows or j < 0 or j >= n_cols or board[i][j] != word[index]:
            return False

        tmp = board[i][j]
        board[i][j] = ""
        operations = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for ix, iy in operations:
            if self.dfs(i+ix, j+iy, n_rows, n_cols, word, index-1, board):
                board[i][j] = tmp
                return True

        board[i][j] = tmp
        return False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        n_rows, n_cols = len(board), len(board[0])
        dictionary = [[] for _ in range(26)]

        for i in range(n_rows):
            for j in range(n_cols):
                dictionary[ord(board[i][j])-97].append((i, j))

        result = []
        for word in words:
            length = len(word)
            for i, j in dictionary[ord(word[-1])-97]:
                if self.dfs(i, j, n_rows, n_cols, word, length-1, board):
                    result.append(word)
                    break

        return result