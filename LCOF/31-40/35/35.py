# Definition for a Node.
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

        if not head:
            return head

        node = head.next
        new_node = new_head = Node(head.val)
        dictionary = {head: new_head}

        while node:
            new_node.next = Node(node.val)
            dictionary[node] = new_node.next
            node, new_node = node.next, new_node.next

        dictionary[None] = None
        node, new_node = head, new_head
        while node:
            new_node.random = dictionary[node.random]
            node, new_node = node.next, new_node.next

        return new_head