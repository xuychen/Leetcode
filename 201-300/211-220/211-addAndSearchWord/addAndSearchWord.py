class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.has_word = False

class WordDictionary(object):
    ASCII_a = 97

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """

        node = self.root
        for char in word:
            index = ord(char) - WordDictionary.ASCII_a
            if index not in node.children:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.has_word = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        return self._search(self.root, word, 0, len(word))

    def _search(self, node, word, index, length):
        if not node:
            return False
        if index == length:
            return node.has_word

        ascii = ord(word[index]) - WordDictionary.ASCII_a
        if word[index] != '.':
            return self._search(node.children.get(ascii, None), word, index+1, length)
        else:
            return any(self._search(new_node, word, index+1, length) for new_node in node.children.values())

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)