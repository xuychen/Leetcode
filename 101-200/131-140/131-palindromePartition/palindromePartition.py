class Solution(object):
    def is_palindrome(self, s):
        left, right = 0, len(s)-1

        while (left <= right):
            if (s[left] != s[right]):
                return False
            else:
                left += 1
                right -= 1

        return True

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        result = []
        for index in range(len(s)):
            left = s[:index+1]
            if (self.is_palindrome(left)):
                for right in self.partition(s[index+1:]):
                    result.append([left]+right)

        return result or [[]]