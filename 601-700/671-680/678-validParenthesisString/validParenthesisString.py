class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        asterisks = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
            else:
                asterisks.append(i)

        while stack and asterisks and stack[-1] < asterisks[-1]:
            stack.pop()
            asterisks.pop()

        return not stack