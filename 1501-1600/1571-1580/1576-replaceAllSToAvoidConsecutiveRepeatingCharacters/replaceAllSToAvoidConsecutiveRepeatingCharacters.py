class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = ""
        length = len(s)

        for i, char in enumerate(s):
            next_char = char
            if char == "?":
                next_char = "a"
                if i > 0 and result[-1] == "a":
                    next_char = "b"
                if i < length - 1 and s[i+1] == next_char:
                    next_char = chr(ord(next_char)+1)
                if i > 0 and result[-1] == next_char:
                    next_char = chr(ord(next_char)+1)

            result += next_char

        return result