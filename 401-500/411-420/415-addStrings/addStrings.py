class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        length1, length2 = len(num1), len(num2)
        if length1 > length2:
            num1, num2 = num2, num1
            length1, length2 = length2, length1

        carry = 0
        result = ""

        for i in range(length2):
            left = int(num1[length1-i-1]) if length1 - i - 1 >= 0 else 0
            right = int(num2[length2-i-1])
            summation = left + right + carry
            carry = summation / 10
            result += str(summation % 10)

        return (result + str(carry) * bool(carry))[::-1]