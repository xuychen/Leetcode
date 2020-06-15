class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if not num:
            return 'Zero'

        thousands = ['', 'Thousand', 'Million', 'Billion']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        digits = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

        thousand_index = 0
        index = 0
        string = ''
        flag = False

        while num > 0:
            if index == 0:
                number = num % 100
                num /= 100
                ten = number / 10
                digit = number % 10


                if number and not flag:
                    string = thousands[thousand_index] + bool(thousands[thousand_index]) * ' ' + string
                    flag = True

                if ten == 1:
                    string = teens[digit] + ' ' + string
                else:
                    string = tens[ten] + ' ' * bool(tens[ten]) + digits[digit] + ' ' * bool(digits[digit]) + string

                index = 2
            else:
                digit = num % 10
                num /= 10

                if digit and not flag:
                    string = thousands[thousand_index] + bool(thousands[thousand_index]) * ' ' + string

                string = digits[digit] + bool(digits[digit]) * ' Hundred ' + string
                flag = False
                thousand_index += 1
                index = 0

        return string[:-1]