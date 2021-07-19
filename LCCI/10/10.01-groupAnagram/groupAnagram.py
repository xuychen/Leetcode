from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        slots = defaultdict(list)
        ASCII_A = 97

        for word in strs:
            index = [0] * 26
            for char in word:
                index[ord(char)-ASCII_A] += 1

            slots[tuple(index)].append(word)

        return slots.values()