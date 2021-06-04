from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        length = len(s)
        char_left = Counter(s)
        stack_chars = set()
        stack = []

        for char in s:
            if char not in stack_chars:
                while len(stack) > 0 and stack[-1] > char and char_left[stack[-1]] > 0:
                    stack_chars.remove(stack.pop())

                stack_chars.add(char)
                stack.append(char)

            char_left[char] -= 1
            
        return ''.join(stack)