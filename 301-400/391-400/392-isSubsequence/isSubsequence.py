class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        head1 = head2 = 0
        length1, length2 = len(s), len(t)

        while head1 < length1 and head2 < length2:
            if s[head1] == t[head2]:
                head1 += 1
                head2 += 1
            else:
                head2 += 1

        return head1 == length1