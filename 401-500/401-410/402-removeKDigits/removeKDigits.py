class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        nums = list(num)

        for i in range(k):
            prev = "0"
            for i, digit in enumerate(nums):
                if prev > digit:
                    del nums[i-1]
                    break

                prev = digit
            else:
                nums.pop()

        return "".join(rstack).lstrip("0") or "0"

    # with stack
    def removeKdigits2(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack, rstack = list(num[::-1]), []
        counter = 0

        rstack.append(stack.pop())

        while counter < k:
            if not rstack or (stack and rstack[-1] <= stack[-1]):
                rstack.append(stack.pop())
            else:
                rstack.pop()
                counter += 1

        while stack:
            rstack.append(stack.pop())

        return "".join(rstack).lstrip("0") or "0"