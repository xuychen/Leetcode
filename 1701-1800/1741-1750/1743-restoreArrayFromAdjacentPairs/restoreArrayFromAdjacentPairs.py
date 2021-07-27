class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """

        adjacency_list = {}
        start_point = 0
        result = []

        for start, end in adjacentPairs:
            adjacency_list.setdefault(start, [])
            adjacency_list.setdefault(end, [])
            adjacency_list[start].append(end)
            adjacency_list[end].append(start)

        for key, values in adjacency_list.items():
            if len(values) == 1:
                start_point = key
                break

        result.append(start_point)
        start_point = adjacency_list[start_point][0]
        result.append(start_point)

        for i in xrange(2, len(adjacency_list)):
            start_point = adjacency_list[start_point][0] if adjacency_list[start_point][0] != result[i-2] else adjacency_list[start_point][1]
            result.append(start_point)

        return result