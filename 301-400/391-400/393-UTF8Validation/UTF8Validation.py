class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        lasting = 0

        for num in data:
            if lasting:
                if num & 128 and not num & 64:
                    lasting -= 1
                else:
                    return False
            else:
                check = 128
                while num & check:
                    lasting += 1
                    check >>= 1

                if lasting == 1 or lasting > 4:
                    return False
                elif lasting:
                    lasting -= 1

        return not lasting