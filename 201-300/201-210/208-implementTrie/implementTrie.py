class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.has_word = False

class Trie(object):
    ASCII_a = 97

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """

        node = self.root
        for char in word:
            index = ord(char) - Trie.ASCII_a
            if index not in node.children:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.has_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node = self.root
        for char in word:
            index = ord(char) - Trie.ASCII_a
            if index not in node.children:
                return False

            node = node.children[index]

        return node.has_word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self.root
        for char in prefix:
            index = ord(char) - Trie.ASCII_a
            if index not in node.children:
                return False

            node = node.children[index]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)