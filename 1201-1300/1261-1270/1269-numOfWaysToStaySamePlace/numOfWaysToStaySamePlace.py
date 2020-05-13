class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """

        arrSize = min((steps + 2) / 2, arrLen)
        array = [0] * arrSize
        array[0] = 1
        new_array = [0] * arrSize

        for _ in range(steps):
            new_array[0] = array[0]
            for i in range(arrSize):
                if i != 0:
                    new_array[i-1] = (new_array[i-1] + array[i]) % (1e9 + 7)
                if i != arrSize - 1:
                    new_array[i+1] = (array[i] + array[i+1]) % (1e9 + 7)

            array, new_array = new_array, array

        return int(array[0])