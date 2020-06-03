class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dictionary, dictionary2 = {}, {}
        length = len(s)

        if length != len(t):
            return False

        for i in range(length):
            lchar, rchar = s[i], t[i]
            dictionary.setdefault(lchar, rchar)
            dictionary2.setdefault(rchar, lchar)

            if dictionary[lchar] != rchar or dictionary2[rchar] != lchar:
                return False

        return True