class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        result = [0]
        i = 1
        
        while 2 ** i <= num:
            for j in range(len(result)):
                result.append(1+result[j])

            i += 1

        for j in range(num+1-2**(i-1)):
            result.append(1+result[j])

        return result