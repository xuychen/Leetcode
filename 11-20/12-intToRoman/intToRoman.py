class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
           
        string = str(num)
        result = ""
        ASCII0 = 48
        
        for i in range(len(string)):
            if i == 0:
                primary = "V"
                secondary = "I"
            elif i == 1:
                primary = "L"
                secondary = "X"
            elif i == 2:
                primary = "D"
                secondary = "C"
            else:
                primary = ""
                secondary = "M"
            
            result = self.digitToRoman(ord(string[len(string)-1-i]) - ASCII0, primary, secondary) + result
        return result
            
        
    def digitToRoman(self, digit, primary, secondary):
        if digit == 0:
            return ""
        elif digit < 4:
            return secondary * digit
        elif digit <= 5:
            return secondary * (5 - digit) + primary
        elif digit < 9:
            return primary + (digit - 5) * secondary
        else:
            if primary == "V":
                primary = "X"
            elif primary == "L":
                primary = "C"
            else:
                primary = "M"
                
            return secondary * (10 - digit) + primary