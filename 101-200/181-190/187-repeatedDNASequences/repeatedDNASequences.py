class SuffixTrieNode(object):
    def __init__(self):
        self._count = 0
        self.children = dict()

class Solution(object):
    def dfs(self, node, string):
        if not node.children and node._count > 1:
            return [string]

        return sum([self.dfs(child, string+char) for char, child in node.children.items()], [])


    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        WINODW_SIZE = 10
        root = SuffixTrieNode()

        for i in range(len(s)-WINODW_SIZE+1):
            node = root
            for j in range(WINODW_SIZE):
                if s[i+j] not in node.children:
                    node.children[s[i+j]] = SuffixTrieNode()

                node = node.children[s[i+j]]

            node._count += 1

        return self.dfs(root, "")

class Solution2(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        dictionary = {}
        length = len(s)
        result = []

        if length <= 10:
            return []

        for i in range(length-9):
            seg = s[i:i+10]
            if seg not in dictionary:
                dictionary[seg] = True
            elif dictionary[seg]:
                result.append(seg)
                dictionary[seg] = False

        return result