# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import randint

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """

        self.linkedlist = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """

        node = self.linkedlist
        num = node.val
        counter = 1

        while node.next:
            node = node.next
            if randint(1, 1+counter) == counter:
                num = node.val

            counter += 1

        return num


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()