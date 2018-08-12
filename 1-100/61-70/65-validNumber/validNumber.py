class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip()
        return self.isNumberHelper(s, len(s), 0, True, False, False, False)
    
    def isNumberHelper(self, s, length, start, numberRequired, hasSign, isFloat, hasE):
        if start < length and s[start] in {"-", "+"}:
            return not hasSign and self.isNumberHelper(s, length, start+1, numberRequired, True, isFloat, hasE)
            
        for i in range(start, length):
            if s[i] == ".":
                return not isFloat and self.isNumberHelper(s, length, i+1, not (i>0 and s[i-1].isdigit()), True, True, hasE)
            elif s[i] == "e":
                return not (hasE or numberRequired) and self.isNumberHelper(s, length, i+1, True, False, True, True)
            elif s[i].isdigit():
                numberRequired = False
            else:
                return False
                
        return not numberRequired