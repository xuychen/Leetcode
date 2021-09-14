class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        index_dictionary = map(lambda x: [x, 0, len(x)], sorted(d, key=lambda x: (-len(x), x)))

        for char in s:
            for dictionary in index_dictionary:
                string, start, end = dictionary[0], dictionary[1], dictionary[2]
                if start != end and char == string[start]:
                    dictionary[1] += 1

        for dictionary in index_dictionary:
            if dictionary[1] == dictionary[2]:
                return dictionary[0]

        return ""

    # others' answer from solution
    def findLongestWord2(self, s, d):
        for word in sorted(d, key = lambda w: (-len(w), w)):
            it = iter(s)
            if all(c in it for c in word): return word
        return ''

class TrieNode(object):
    def __init__(self, c):
        self.char = c
        self.children = [None] * 26

    def add_child(self, node):
        self.children[ord(node.char)-97] = node

    def find_child(self, c):
        return self.children[ord(c)-97]

class Solution2(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """

        length = len(s)
        candidates = TrieNode("")
        result = ""

        for i in range(length-1, -1, -1):
            node = TrieNode(s[i])
            for candidate in candidates.children:
                if candidate:
                    node.add_child(candidate)

            candidates.add_child(node)

        for target in sorted(dictionary):
            node = candidates
            for char in target:
                node = node.find_child(char)
                if not node:
                    break

            if node and len(target) > len(result):
                result = target

        return result