import bisect

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.hash_set = {}


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        if key not in self.hash_set:
            self.hash_set[key] = []

        self.hash_set[key].append((timestamp, value))


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        if key in self.hash_set:
            index = bisect.bisect(self.hash_set[key], (timestamp+1, ""))
            return self.hash_set[key][index-1][1] if index else ""

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)