class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        count = 1

        for num in preorder.split(','):
            if not count:
                return False
            elif num != '#':
                count += 1
            else:
                count -= 1

        return count == 0