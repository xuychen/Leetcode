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
        queue = []
        
        if root:
            queue.append(root)
        
        while queue != []:
            newQueue = []
            queueCount = len(queue)
            queue.append(None)
            for i in range(queueCount):
                elem = queue[i]
                if elem.left:
                    newQueue.append(elem.left)
                if elem.right:
                    newQueue.append(elem.right)
                elem.next = queue[i+1]
            queue = newQueue