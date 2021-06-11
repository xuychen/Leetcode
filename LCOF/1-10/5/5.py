class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_string = ""

        for char in s:
            if char != ' ':
                new_string += char
            else:
                new_string += '%20'

        return new_string