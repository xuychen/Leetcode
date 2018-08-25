# dp solution with space complexity S(1)

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        pprev, prev, curr = 0, 1, 1
        prevNum = "3"
                
        for i, digit in enumerate(s):
            if digit == "0":
                if prevNum not in {"1", "2"}:
                    return 0
                else:
                    curr = pprev
            elif 10 < int(prevNum+digit) <= 26:
                curr += pprev
                
            prevNum = digit
            pprev = prev
            prev = curr
            
        return curr if s else 0