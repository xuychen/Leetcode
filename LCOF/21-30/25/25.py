# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1 or not l2:
            return l1 or l2

        new_list = new_list_head = None
        if l1.val < l2.val:
            new_list = new_list_head = l1
            l1 = l1.next
        else:
            new_list = new_list_head = l2
            l2 = l2.next

        while l1 and l2:
            if l1.val < l2.val:
                new_list.next = l1
                l1 = l1.next
            else:
                new_list.next = l2
                l2 = l2.next

            new_list =  new_list.next

        new_list.next = l1 or l2
        return new_list_head