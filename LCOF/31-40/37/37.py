import Queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = []
        qe = Queue.Queue(maxsize=0)
        qe.put(root)

        while not qe.empty():
            node = qe.get()
            if not node:
                result.append("None")
            else:
                result.append(str(node.val))
                qe.put(node.left)
                qe.put(node.right)

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        qe = Queue.Queue(maxsize=0)
        split_data = data.split(",")

        root = TreeNode(split_data[0]) if split_data[0] != "None" else None
        index = 1
        length = len(split_data)
        qe.put(root)

        while index < length:
            node = qe.get()
            if split_data[index] != "None":
                node.left = TreeNode(int(split_data[index]))
                qe.put(node.left)
            if split_data[index+1] != "None":
                node.right = TreeNode(int(split_data[index+1]))
                qe.put(node.right)

            index += 2

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))