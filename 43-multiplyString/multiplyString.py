ASCII0 = 48

class Solution(object):
    def multiplyByDigit(self, digit, num):
        """
        :type num1: str
        :type num2: str
        :rtype: [int]
        """
        
        nums = [0] * len(num)
        aDigit = ord(digit) - ASCII0
        
        for index in range(len(num)-1, -1, -1):
            chr = num[index]
            bDigit = ord(chr) - ASCII0
            result = aDigit * bDigit
            nums[index] = result
            
        return nums
        
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        # shrink time for get rid of leading 0
        if num1 == "0" or num2 == "0":
            return "0"
        
        length2 = len(num2)
        result = [0] * (len(num1) + length2)
        
        # adding
        for index in range(len(num1)-1, -1, -1):
            chr = num1[index]
            oneResult = self.multiplyByDigit(chr, num2)
            for pos in range(0, len(oneResult)):
                result[length2+index-len(oneResult)+1+pos] += oneResult[pos]
        
        
        # moving forward
        carryOn = 0
        for index in range(len(result)-1, -1, -1):
            newNum = result[index] + carryOn
            result[index] = newNum % 10
            carryOn = (newNum - result[index]) / 10
        
        
        # get rid of leading 0
        i = 0 
        while result[i] == 0:
            i += 1
        
        return ''.join(str(x) for x in result[i:])