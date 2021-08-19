class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        absence = 0
        late = 0

        for char in s:
            if char == "A":
                late = 0
                absence += 1
            elif char == "L":
                late += 1
                if late == 3:
                    return False
            else:
                late = 0

        return late < 3 and absence < 2