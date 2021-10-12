class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = []

        for i in range(1, n+1):
            result.append(("" if i % 3 else "Fizz") + ("" if i % 5 else "Buzz") or str(i))

        return result

    def fizzBuzz2(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

    def fizzBuzz3(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        result = ["" for _ in range(n)]
        for i in range(1, n+1):
            if i % 3 == 0:
                result[i-1] += "Fizz"
            if i % 5 == 0:
                result[i-1] += "Buzz"
            if not result[i-1]:
                result[i-1] += str(i)

        return result