# The rand7() API is already defined for you.
def rand7():
    return 1
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        num = 0

        while num == 0 or num >= 11:
            num = 0
            count = 0
            while count < 4:
                n = 7
                while n == 7:
                    n = rand7()

                num <<= 1
                num += n & 1
                count += 1

        return num