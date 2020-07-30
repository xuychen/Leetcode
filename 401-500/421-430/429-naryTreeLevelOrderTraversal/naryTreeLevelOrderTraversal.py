import Queue

class Solution(object):
    def levelOrder(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        qe = Queue.Queue(maxsize=0)
        new_qe = Queue.Queue(maxsize=0)
        result = []

        if root:
            new_qe.put(root)

        while not new_qe.empty():
            qe, new_qe = new_qe, qe
            level = []
            while not qe.empty():
                node = qe.get()
                level.append(node.val)

                for child in node.children:
                    if child:
                        new_qe.put(child)

            result.append(level)

        return result