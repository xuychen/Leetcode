# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head.next if head else None
        start = head
        prev = None
        flag = False

        while node:
            if node.val == start.val:
                start.next = node.next
                flag = True
            else:
                if flag:
                    if prev:
                        prev.next = node
                    else:
                        head = node
                else:
                    prev = start

                start = node
                flag = False
            node = start.next

        if flag:
            if prev:
                prev.next = node
            else:
                head = node
        return head

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(None, head)
        start, end = dummy, head
        count = 0

        while end:
            if start.next.val == end.val:
                count += 1
            elif count > 1:
                start.next = end
                count = 1
            else:
                start = start.next
                count = 1

            end = end.next

        if count > 1:
            start.next = end

        return dummy.next