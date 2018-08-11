class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        s += "." # in case of out of range
        for i in range(len(s)-1):
            chr = s[i]
            if chr == "M":
                res += 1000
            elif chr == "D":
                res += 500
            elif chr == "C":
                if s[i+1] == "M" or s[i+1] == "D":
                    res -= 100
                else:
                    res += 100
            elif chr == "L":
                res += 50
            elif chr == "X":
                if s[i+1] == "C" or s[i+1] == "L":
                    res -= 10
                else:
                    res += 10
            elif chr == "V":
                res += 5
            else:
                if s[i+1] == "V" or s[i+1] == "X":
                    res -= 1
                else:
                    res += 1
                    
        return res