class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        string = ""
        times = 0
        stack = []

        for char in s:
            if char.isalpha():
                string += char
            elif char.isdigit():
                times = times * 10 + int(char)
            elif char == '[':
                stack.append(string)
                stack.append(times)
                string = ""
                times = 0
            else:
                string *= stack.pop()
                string = stack.pop() + string

        return string