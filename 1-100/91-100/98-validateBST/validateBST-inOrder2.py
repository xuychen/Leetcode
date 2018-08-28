# faster version than the first one

class Solution:
    def isValidBST(self, root):
        return self.isValidBSTHelper(root, -float('inf'))[0]
        
    def isValidBSTHelper(self, root, prev):
        if root:
            resL, prev = self.isValidBSTHelper(root.left, prev)
            resC = prev < root.val
            return self.isValidBSTHelper(root.right, root.val) if resL and resC else (False, prev)
        return True, prev