# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[L
        ist[int]]
        :rtype: Node
        """

        length = len(grid)
        return self.construct_helper(grid, 0, length, 0, length)

    def construct_helper(self, grid, x_start, x_end, y_start, y_end):
        if x_start == x_end - 1:
            return Node(grid[x_start][y_start], True, None, None, None, None)

        x_mid, y_mid = (x_start + x_end) / 2, (y_start + y_end) / 2
        top_left = self.construct_helper(grid, x_start, x_mid, y_start, y_mid)
        top_right = self.construct_helper(grid, x_start, x_mid, y_mid, y_end)
        bottom_left = self.construct_helper(grid, x_mid, x_end, y_start, y_mid)
        bottom_right = self.construct_helper(grid, x_mid, x_end, y_mid, y_end)

        if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf:
            summation = top_left.val + top_right.val + bottom_left.val + bottom_right.val
            if summation % 4 == 0:
                return Node(summation / 4, True, None, None, None, None)

        return Node(1, False, top_left, top_right, bottom_left, bottom_right)