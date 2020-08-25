class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        power = 1
        while power <= num:
            power <<= 1
            
        return power - 1 - num