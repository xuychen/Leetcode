class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            head = root
            while head.left:
                p = head
                while p:
                    p.left.next = p.right
                    if p.next:
                        p.right.next = p.next.left
                    p = p.next
                head = head.left