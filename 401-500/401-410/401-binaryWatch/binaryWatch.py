class Solution(object):
    def __init__(self):
        self.hour = [[0]]
        self.minute = [[0]]

        hours = [1,2,4,8]
        minutes = [1,2,4,8,16,32]

        for i in range(1, 4):
            self.hour.append(filter(lambda x: x < 12, map(sum, itertools.combinations(hours, i))))

        for i in range(1, 6):
            self.minute.append(filter(lambda x: x < 60, map(sum, itertools.combinations(minutes, i))))

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        result = []

        for i in range(min(num, 3), -1, -1):
            if num - i == 6:
                break

            for hour in self.hour[i]:
                for minute in self.minute[num-i]:
                    result.append("{}:{:02}".format(hour, minute))

        return result