import re

class Solution(object):
    def reverseVowels(self, s):
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """

        start, end = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        array = list(s)

        while start < end:
            if s[start] not in vowels:
                start += 1
            elif s[end] not in vowels:
                end -= 1
            else:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1

        return ''.join(array)