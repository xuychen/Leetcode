# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        odd_node = dummy_head = ListNode(None)
        even_node = dummy_head2 = ListNode(None)
        node = head

        while node and node.next:
            odd_node.next = node
            even_node.next = node.next
            odd_node = odd_node.next
            even_node = even_node.next
            node = even_node.next

        if node:
            odd_node.next = node
            odd_node = odd_node.next
            even_node.next = None

        odd_node.next = dummy_head2.next
        return dummy_head.next