# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        newTail, joint, _ = self.locate(head, None, k, 0)
        newHead = newTail and newTail.next
        if newHead:
            joint.next = head
            newTail.next = None
        return newHead or head


    def locate(self, node, prev, k, length):
        if not node:
            return prev, prev, length and k % length

        tail, joint, back = self.locate(node.next, node, k, length+1)
        return (prev, joint, back-1) if back else (tail, joint, back)

class Solution2(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        end, node = None, head
        length = 0

        while node:
            length += 1
            end = node
            node = node.next

        if length:
            index = length - k % length
            prev, node = None, head
            for i in range(index):
                prev = node
                node = node.next

            end.next = head
            prev.next = None

        return node or head