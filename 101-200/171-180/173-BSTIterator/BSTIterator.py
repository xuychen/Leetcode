# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """

        self.stack = [root]
        self.visited = not root

        node = root
        if node:
            while node.left:
                self.stack.append(node.left)
                node = node.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """

        result = node = self.stack[-1]

        if node.right:
            self.stack.append(node.right)
            node = node.right
            while node.left:
                self.stack.append(node.left)
                node = node.left
        else:
            for i in range(len(self.stack)-2, -1, -1):
                prev = self.stack.pop()
                if self.stack[i].right != prev:
                    break

        if result == self.stack[0]:
            self.visited = True

        return result.val


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """

        return not self.visited or len(self.stack) > 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()