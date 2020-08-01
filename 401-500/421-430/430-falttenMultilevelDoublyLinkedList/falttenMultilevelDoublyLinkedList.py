"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        node = head
        stack = []

        while node:
            if node.child:
                if node.next:
                    stack.append(node.next)

                node.next = node.child
                node.child.prev = node
                node.child = None

            if not node.next and stack:
                node.next = stack.pop()
                node.next.prev = node

            node = node.next

        return head