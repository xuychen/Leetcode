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