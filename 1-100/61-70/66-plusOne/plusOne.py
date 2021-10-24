class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        carry_on = 0
        digits[-1] += 1

        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry_on
            if digits[i] == 10:
                digits[i] = 0
                carry_on = 1
            else:
                carry_on = 0

        return [1] * carry_on + digits