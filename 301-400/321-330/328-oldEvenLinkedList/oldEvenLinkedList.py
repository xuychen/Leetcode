# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        odd = head
        even_head = even = head.next if head else None
        prev = None

        while odd and even:
            prev = odd
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next

        if odd:
            odd.next = even_head
        elif prev:
            prev.next = even_head

        return head