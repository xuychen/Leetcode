class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """

        level = 1
        result = []
        while label >= (1 << level):
            level += 1

        result.append(label)
        while level > 1:
            if level & 1:
                next_label = label / 2
                label = (1 << (level-1)) - next_label + (1 << (level-2)) - 1
            else:
                next_label = (1 << level) - label + (1 << (level-1)) - 1
                label = next_label / 2

            result.append(label)
            level -= 1

        return result[::-1]