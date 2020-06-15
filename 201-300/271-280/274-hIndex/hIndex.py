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