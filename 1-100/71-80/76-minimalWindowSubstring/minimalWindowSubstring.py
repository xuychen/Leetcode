# solution from discussion
import collections

class Solution(object):
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        counter = collections.Counter(t)
        count = len(counter)
        length = len(s)
        i = start = 0

        result = "#" * (length + 1)

        while i < length:
            while count > 0 and i < length:
                char = s[i]
                if char in counter:
                    counter[char] -= 1
                    if counter[char] == 0:
                        count -= 1

                i += 1

            while start < i and (s[start] not in counter or counter[s[start]] < 0):
                if counter[s[start]] < 0:
                    counter[s[start]] += 1

                start += 1

            if count == 0 and i - start < len(result):
                result = s[start:i]

            if start < i:
                counter[s[start]] += 1
                start += 1
                count += 1

        return "" if result == "#" * (length + 1) else result
