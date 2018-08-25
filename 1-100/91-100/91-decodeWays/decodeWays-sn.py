# dp with space complexity S(n)

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        array = [1] + [0] * len(s)
        prevNum = "3"
                
        for i, digit in enumerate(s, 1):
            if digit == "0":
                if prevNum not in {"1", "2"}:
                    return 0
                else:
                    array[i] = array[i-2]
            else:
                array[i] = array[i-1] + array[i-2] if 10 < int(prevNum+digit) <= 26 else array[i-1]
            prevNum = digit
            
        return array[-1] if s else 0