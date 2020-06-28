class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        length = len(num)
        if length < 3:
            return False

        for i in range(length/2):
            if num[0] == '0' and i > 0:
                break

            for j in range(i+1, 2*length/3):
                if num[i+1] == '0' and j - i > 1:
                    break

                first = int(num[:i+1])
                second = int(num[i+1:j+1])
                end = j+1

                while end < length:
                    summation = first + second
                    str_sum = str(summation)
                    if not num.startswith(str_sum, end):
                        break

                    end += len(str_sum)
                    first, second = second, summation

                if end == length:
                    return True

        return False