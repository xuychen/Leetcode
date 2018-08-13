class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        aLength, bLength = len(a), len(b)
        if aLength > bLength:
            b = "0" * (aLength - bLength) + b
            bLength = aLength
        else:
            a = "0" * (bLength - aLength) + a
            aLength = bLength
            
        carryOn = 0
        result = ""
        
        for i in range(aLength-1, -1, -1):
            num1, num2 = int(a[i]), int(b[i])
            result = str(num1 ^ num2 ^ carryOn) + result
            carryOn = (num1 + num2 + carryOn) / 2
        
        return carryOn * str(carryOn) + result
         