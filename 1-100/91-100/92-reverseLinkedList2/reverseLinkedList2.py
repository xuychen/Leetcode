# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        prev, node = None, head
        i = 0
        for i in range(1, m):
            prev = node
            node = node.next

        reverseHead, _ = self.reverse(node, None, n-i, n-i)
        if prev:
            prev.next = reverseHead
        else:
            head = reverseHead

        return head

    def reverse(self, node, prev, index, count):
        if index == 0:
            return prev, node

        reverseHead, tailHead = self.reverse(node.next, node, index-1, count)
        node.next = prev if index != count else tailHead
        return reverseHead, tailHead

class Solution2(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        self.helper(dummy, left, right, 0, None)
        return dummy.next

    def helper(self, node, left, right, index, prev):
        if index > right:
            return prev, node

        head, end = self.helper(node.next, left, right, index+1, node)
        if index > left:
            node.next = prev
        elif index == left:
            node.next = end
            prev.next = head

        return head, end
