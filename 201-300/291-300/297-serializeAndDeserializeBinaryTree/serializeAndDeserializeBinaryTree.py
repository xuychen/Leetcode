# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
                data.append(str(node.val))
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

        myiter = iter(data.split())
        qe = Queue.Queue(maxsize=0)
        item = next(myiter)
        if item == "null":
            return None

        root = TreeNode(int(item))
        qe.put(root)

        while not qe.empty():
            node = qe.get()
            item = next(myiter)
            if item != "null":
                node.left = TreeNode(int(item))
                qe.put(node.left)

            item = next(myiter)
            if item != "null":
                node.right = TreeNode(int(item))
                qe.put(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))