class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        dictionary = defaultdict(bool)
        result = 0

        for char in s:
            if not dictionary[char]:
                dictionary[char] = True
            else:
                dictionary[char] = False
                result += 2

        return any(dictionary.values()) * 1 + result

    # answer from others
    def longestPalindrome2(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)