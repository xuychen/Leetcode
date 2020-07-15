class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        length = len(b)
        base_power = a % 1337
        result = a ** b[-1]
        base = 1

        while base < length:
            base_power = (base_power ** 10) % 1337
            value = base_power ** b[length-1-base] % 1337
            result = (result * value) % 1337
            base += 1

        return result