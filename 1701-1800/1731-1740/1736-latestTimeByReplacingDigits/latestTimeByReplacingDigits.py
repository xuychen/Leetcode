class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        result = ""

        if time[0] == "?":
            if time[1] == "?":
                result += "23"
            elif int(time[1]) > 3:
                result += "1"
            else:
                result += "2"
        else:
            result += time[0]

        if time[1] == "?":
            if time[0] == '2':
                result += "3"
            elif time[0] != "?":
                result += "9"
        else:
            result += time[1]

        result += ":"
        if time[3] == "?":
            result += "5"
        else:
            result += time[3]

        if time[4] == "?":
            result += "9"
        else:
            result += time[4]

        return result