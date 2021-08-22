class Solution(object):
    def l1_distance(self, curr, target):
        return abs(curr[0] - target[0]) + abs(curr[1] - target[1])

    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        distance = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            if self.l1_distance(ghost, target) <= distance:
                return False

        return True