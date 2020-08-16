class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class SuffixTrie(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        node.wordEnd = True

    def findSmallWords(self, node, word):
        result = [word] if node.wordEnd else []

        for char in sorted(node.children.keys()):
            if len(result) >= 3:
                break

            result += self.findSmallWords(node.children[char], word + char)

        return result[:3]

    def searchWordWithPrefix(self, prefix):
        node = self.root
        result = []
        string = ""

        for char in prefix:
            string += char
            node = node and node.children.get(char, None)
            result.append(self.findSmallWords(node, string)  if node else [])

        return result

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        suffixTrie = SuffixTrie()
        for product in products:
            suffixTrie.addWord(product)

        return suffixTrie.searchWordWithPrefix(searchWord)

    # binary search with prefix solution
    def suggestedProducts2(self, A, word):
        A.sort()
        res, prefix, i = [], '', 0
        for c in word:
            prefix += c
            i = bisect.bisect_left(A, prefix, i)
            res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
        return res