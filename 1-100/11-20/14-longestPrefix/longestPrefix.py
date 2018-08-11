class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        
        lens = map(lambda x: len(x), strs)
        minLen = min(lens)
        
        if minLen == 0:
            return ""
        
        ref = strs[0]
        
        i = 0
        for i in range(minLen):
            for string in strs[1:]:
                if ref[i] != string[i]:
                    return ref[:i]
                
        i += 1
        return ref[:i]