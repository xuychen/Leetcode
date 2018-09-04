# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            nextRoot = prev = None
            while root:
                if not nextRoot:
                    nextRoot = root.left
                else:
                    prev.next = root.left
                prev = root.left or prev
                
                if not nextRoot:
                    nextRoot = root.right
                else:
                    prev.next = root.right
                prev = root.right or prev
                root = root.next
            root = nextRoot