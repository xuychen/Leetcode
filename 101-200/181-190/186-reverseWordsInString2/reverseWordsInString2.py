class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        stack = []
        result = []

        for char in s[::-1]:
            if char != " ":
                stack.append(char)
            else:
                while stack:
                    result.append(stack.pop())

                result.append(" ")

        while stack:
            result.append(stack.pop())

        for i, char in enumerate(result):
            s[i] = char
