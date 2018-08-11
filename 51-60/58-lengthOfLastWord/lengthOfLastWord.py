class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start, length = 0, len(s)
        
        while start < length and s[length-start-1] == ' ':
            start += 1
        end = start
        while end < length and s[length-end-1] != ' ':
            end += 1
                
        return end - start