class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        return self.restoreHelper(s, 0, len(s))
        
    def restoreHelper(self, s, index, length, string="", dot=0):
        result = []
        if dot == 3:
            if int(s[index:]) <= 255 and (s[index] != "0" or length == 1):
                return [string + s[index:]]
        else:
            for i in range(1, min(length, 4)):
                num = s[index:index+i]
                if int(num) <= 255 and (s[index] != "0" or i == 1):
                    result += self.restoreHelper(s, index+i, length-i, string+num+".", dot+1)
                
        return result