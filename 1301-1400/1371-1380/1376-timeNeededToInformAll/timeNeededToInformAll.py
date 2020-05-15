class Solution(object):
    def maximum_time(self, node, children, informTime):
        if node not in children:
            return informTime[node]

        max_time = max([self.maximum_time(child, children, informTime) for child in children[node]])
        return max_time + informTime[node]


    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """

        children = {}
        for i, node in enumerate(manager):
            children.setdefault(node, [])
            children[node].append(i)

        return self.maximum_time(headID, children, informTime)
