import itertools

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        ver1s = map(int, version1.split("."))
        ver2s = map(int, version2.split("."))
        diff = len(ver1s) - len(ver2s)
        negative = 1

        if diff > 0:
            negative = -1
            ver1s, ver2s = ver2s, ver1s

        for i in range(len(ver1s)):
            if ver1s[i] > ver2s[i]:
                return 1 * negative
            elif ver1s[i] < ver2s[i]:
                return -1 * negative

        for j in range(i+1, len(ver2s)):
            if ver2s[j] > 0:
                return -1 * negative

        return 0


    def compareVersion2(self, version1, version2):
        splits = (map(int, v.split('.')) for v in (version1, version2))
        return cmp(*zip(*itertools.izip_longest(*splits, fillvalue=0)))