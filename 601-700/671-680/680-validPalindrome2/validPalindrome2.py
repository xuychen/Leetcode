class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        return self.validPalindromeHelper(s, 0, len(s)-1, True)
        
    def validPalindromeHelper(self, s, left, right, chance):
        while right - left > 0:
            if s[left] != s[right]:
                return chance and (self.validPalindromeHelper(s, left+1, right, False) or self.validPalindromeHelper(s, left, right-1, False))
            
            left += 1
            right -= 1
            
        return True