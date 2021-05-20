# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry_on = 0
        l3 = l3_head = None

        while l1 or l2 or carry_on:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0

            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            summation = l1_val + l2_val + carry_on

            if summation >= 10:
                summation -= 10
                carry_on = 1
            else:
                carry_on = 0

            if l3:
                l3.next = ListNode(summation)
                l3 = l3.next
            else:
                l3 = l3_head = ListNode(summation)

        return l3_head
