import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.has_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]

        node.has_word = True

class Solution(object):
    def dfs(self, i, j, rows, cols, board, node, string):
        result = []
        if not node:
            return result

        if node.has_word:
            node.has_word = False
            result.append(string)

        if  i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] == '#':
            return result

        char, board[i][j] = board[i][j], '#'
        node = node.children.get(char, None)

        result += self.dfs(i-1, j, rows, cols, board, node, string+char) \
                + self.dfs(i, j-1, rows, cols, board, node, string+char) \
                + self.dfs(i+1, j, rows, cols, board, node, string+char) \
                + self.dfs(i, j+1, rows, cols, board, node, string+char)

        board[i][j] = char
        return result

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        rows = len(board)
        cols = len(board[0])
        trie = Trie()
        result = []
        for word in words:
            trie.insert(word)

        for i in range(rows):
            for j in range(cols):
                result += self.dfs(i, j, rows, cols, board, trie.root, "")

        return result