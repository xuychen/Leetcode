class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        strings = str.split()
        a2b, b2a = {}, {}

        if len(pattern) != len(strings):
            return False

        for i, string in enumerate(strings):
            a2b.setdefault(string, pattern[i])
            b2a.setdefault(pattern[i], string)

            if pattern[i] != a2b[string] or b2a[pattern[i]] != string:
                return False

        return True