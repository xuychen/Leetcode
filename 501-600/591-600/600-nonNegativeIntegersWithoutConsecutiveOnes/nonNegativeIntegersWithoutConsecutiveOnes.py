class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """

        zeros = [1]
        ones = [1]
        shift = 0
        flag = False
        consecutive = set()

        while n >= (1 << shift):
            zeros.append(zeros[-1]+ones[-1])
            ones.append(zeros[-2])
            if n & (1 << shift):
                if flag:
                    consecutive.add(shift)

                flag = True
            else:
                flag = False

            shift += 1

        shift = 0
        result = int(not consecutive)

        while n >= (1 << shift):
            if n & (1 << shift):
                if shift + 1 in consecutive:
                    consecutive.remove(shift+1)
                if not consecutive:
                    result += zeros[shift]

            shift += 1

        return result


    # 作者：LeetCode-Solution
    # 链接：https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/solution/bu-han-lian-xu-1de-fei-fu-zheng-shu-by-l-9l86/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    # better than my solution, yet the idea is the same
    def findIntegers2(self, n):
        dp = [0] * 31
        dp[0] = 1
        dp[1] = 1
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]

        pre = 0
        res = 0

        for i in range(29, -1, -1):
            val = (1 << i)
            if n & val:
                res += dp[i + 1]
                if pre == 1:
                    break
                pre = 1
            else:
                pre = 0

            if i == 0:
                res += 1

        return res