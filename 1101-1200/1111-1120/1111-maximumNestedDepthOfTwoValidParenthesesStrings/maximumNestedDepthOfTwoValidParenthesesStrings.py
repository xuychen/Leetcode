class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

        result = [0] * len(seq)
        depth = 0
        max_depth = self.maxDepth(seq)

        for i in range(len(seq)-1, -1, -1):
            char = seq[i]
            if char == ")":
                if depth < max_depth / 2:
                    result[i] = 1
                    depth += 1
            else:
                if depth > 0:
                    result[i] = 1
                    depth -= 1

        return result

    def maxDepth(self, s):
        maximum = depth = 0
        stack = []

        for char in s:
            depth += (-1, 1)[char == '(']
            maximum = max(maximum, depth)

        return maximum

class Solution2(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

        depth = 0
        result = []

        for char in seq:
            if char == "(":
                depth += 1
                result.append(depth & 1)
            else:
                result.append(depth & 1)
                depth -= 1

        return result