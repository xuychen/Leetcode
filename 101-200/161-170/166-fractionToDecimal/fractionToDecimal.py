class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        negative = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        integral = numerator // denominator
        remainder = numerator % denominator
        fractional = ""
        dictionary = {}
        index = 0

        while remainder > 0:
            if remainder in dictionary:
                start = dictionary[remainder]
                fractional = fractional[:start] + '(' + fractional[start:] + ')'
                return negative * "-" + str(integral) + '.' + fractional
            else:
                dictionary[remainder] = index

            remainder *= 10
            quotient = remainder // denominator
            remainder = remainder % denominator
            fractional += str(quotient)
            index += 1

        return negative * "-" + str(integral) + ('.' + fractional if fractional else '')