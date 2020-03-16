"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        new_head = new_end = None
        dictionary = {None: None}

        node = head
        while node:
            if new_head:
                new_end.next = Node(node.val, None, node.random)
                new_end = new_end.next
            else:
                new_head = new_end = Node(node.val, None, node.random)

            dictionary[node] = new_end
            node = node.next

        node = new_head
        while node:
            node.random = dictionary[node.random]
            node = node.next

        return new_head