class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def arrayToTree(array):
    if array == [] or array[0] == "null":
        return None

    queue = []
    queueBack, queueFront = 0, 1
    root = parentNode = TreeNode(array[0])

    for i in range(1, len(array)):
        elem = array[i]
        node = None if elem == "null" else TreeNode(elem)
        if node:
            queue.append(node)
            queueFront += 1

        if i & 1:
            parentNode.left = node
        else:
            parentNode.right = node
            parentNode = queue[queueBack]
            queueBack += 1

    return root

def levelOrderCheck(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
         
        queue = []
        result = []
        queueFront = queueBack = 0
        
        if root:
            queue.append(root)
            queueFront += 1
            result.append([root.val])
        
        while queueBack < queueFront:
            increase = 0
            while queueBack < queueFront:
                node = queue[queueBack]
                queueBack += 1
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    increase += 2
            if increase:
                queueFront += increase
                result.append(map(lambda x: (x and x.val), queue[queueBack: queueFront]))
        
        return result

        
root = arrayToTree([1,-2,-3,1,3,-2,"null",-1])
print(levelOrderCheck(root))