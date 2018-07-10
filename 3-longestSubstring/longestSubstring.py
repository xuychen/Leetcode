class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        index = 0
        result = 0
        count = 0
        cutline = -1
        dictionary = {}
        
        while index < len(s):
            chr = s[index]
            oldIndex = dictionary.get(chr, -1)
            if oldIndex == -1 or cutline >= oldIndex:
                dictionary[chr] = index
                count += 1
            else:
                if result < count:
                    result = count
                    
                count = index - dictionary[chr]
                cutline = dictionary[chr]
                dictionary[chr] = index
                
            index += 1
            
        if count > result:
            result = count
        return result
                
        