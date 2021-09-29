class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        if C <= E or G <= A:
            width = 0
        elif E <= A and C <= G:
            width = C - A
        elif A <= E and G <= C:
            width = G - E
        elif G > C:
            width = C - E
        else:
            width = G - A

        if H <= B or D <= F:
            height = 0
        elif F <= B and D <= H:
            height = D - B
        elif B <= F and H <= D:
            height = H - F
        elif H > D:
            height = D - F
        else:
            height = H - B

        return (D - B) * (C - A) + (H - F) * (G - E) - width * height

    def computeArea2(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        ix1 = max(ax1, bx1)
        iy1 = max(ay1, by1)
        ix2 = min(ax2, bx2)
        iy2 = min(ay2, by2)
        iarea = max(0, ix2 - ix1) * max(0, iy2 - iy1)
        return area1 + area2 - iarea