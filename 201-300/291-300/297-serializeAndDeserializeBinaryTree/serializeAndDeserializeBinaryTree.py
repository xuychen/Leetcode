# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import Queue

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        qe = Queue.Queue(maxsize=0)
        qe.put(root)
        data = []

        while not qe.empty():
            node = qe.get()

            if node:
                data.append(node.val)
                qe.put(node.left)
                qe.put(node.right)
            else:
                data.append("null")

        return " ".join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        array = data.split()
        qe = Queue.Queue(maxsize=0)
        if array[0] == "null":
            return None

        root = TreeNode(int(array[0]))
        index = 1
        qe.put(root)

        while not qe.empty():
            node = qe.pop()
            if array[index] != "null":
                node.left = TreeNode(int(array[index]))
                qe.put(node.left)
                index += 1

            if array[index] != "null":
                node.right = TreeNode(int(array[index]))
                qe.put(node.right)
                index += 1

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))