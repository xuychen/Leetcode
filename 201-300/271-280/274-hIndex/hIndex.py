class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        sorted_citations = sorted(citations)
        length = len(citations)
        maximum = 0

        for i, value in enumerate(sorted_citations):
            if maximum >= length - i:
                break

            maximum = min(value, length - i)

        return maximum

    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        sort_citations = sorted(citations, reverse=True)
        count = 0

        for citation in sort_citations:
            if citation > count:
                count += 1
            else:
                break
            
        return count


class Solution2:
    # linear time algorithm
    def hIndex(self, citations):
        n = len(citations); tot = 0
        counter = [0] * (n+1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/h-index/solution/h-zhi-shu-by-leetcode-solution-fnhl/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。