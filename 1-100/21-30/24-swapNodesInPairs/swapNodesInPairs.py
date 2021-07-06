# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head and head.next:
            head = self.swapTwo(head)
            node = head.next

            while node.next and node.next.next:
                node.next = self.swapTwo(node.next)
                node = node.next.next

        return head

    def swapTwo(self, node):
        next = node.next
        tmp = next.next
        next.next = node
        next.next.next = tmp
        return next

class Solution2(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy_head = ListNode(None)
        new_list = dummy_head

        node = next_node = head
        while node:
            tmp = node.next and node.next.next
            if node.next:
                tmp = node.next.next
                new_list.next = node.next
                new_list = new_list.next

            new_list.next = node
            node.next = tmp
            new_list = new_list.next
            node = tmp

        return dummy_head.next