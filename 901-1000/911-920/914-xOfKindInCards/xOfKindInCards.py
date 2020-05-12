from collections import Counter

class Solution(object):
    # answer from others' inspiration
    def gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2

        return num1

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        return reduce(self.gcd, Counter(deck).values()) > 1

    def gcd2(self, num1, num2):
        if num1 > num2:
            return self.gcd(num2, num1)

        while num1 != num2:
            diff = num2 - num1
            if diff < num1:
                num2 = num1
                num1 = diff
            else:
                num2 = diff

        return num1

    def hasGroupsSizeX2(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        initializer = 1
        value_set = set()
        for _, value in Counter(deck).items():
            value_set.add(value)
            initializer = value

        return reduce(lambda x, y: self.gcd(x, y), value_set, initializer) != 1