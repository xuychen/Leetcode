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