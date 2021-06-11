import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        return bool(re.match('^[+-]?(\d*\.?\d*|\d+\.)([eE][+-]?\d+)?$', s.strip()))