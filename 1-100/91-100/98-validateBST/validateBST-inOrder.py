# done by in order traversal

class Solution:
    def __init__(self):
        self.prev = -float('inf')
        
    def isValidBST(self, root):
        if root:
            resLC = self.isValidBST(root.left) and self.prev < root.val
            self.prev = root.val
            return resLC and self.isValidBST(root.right)
        return True