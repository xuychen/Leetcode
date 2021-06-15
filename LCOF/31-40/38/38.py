class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if not s:
            return [""]

        result = []
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                rhs = self.permutation(s[:i]+ s[i+1:])
                for elem in rhs:
                    result.append(s[i]+elem)

        return result