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

    def addBinary2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        carryOn = 0
        i, j = len(a) - 1, len(b) - 1
        result = ""

        while i >= 0 or j >= 0 or carryOn:
            summation = (int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0) + carryOn
            carryOn = summation >= 2
            summation &= 1
            result += str(summation)
            i -= 1
            j -= 1

        return result[::-1]
