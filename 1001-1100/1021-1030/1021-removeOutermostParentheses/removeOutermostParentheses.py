class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        result = ""

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char == ')':
                    stack.pop()
                else:
                    stack.append(char)
                if stack:
                    result += char

        return result