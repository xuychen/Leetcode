# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        track = []
        single = double = head

        while double:
            track.append(single.val)
            single = single.next
            if double.next:
                double = double.next.next
            else:
                double = double.next
                track.pop()

        while single:
            if single.val != track.pop():
                return False

            single = single.next

        return True