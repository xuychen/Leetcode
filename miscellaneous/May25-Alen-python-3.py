import Queue

# assume the level where root is in is level 0
def compute_median(alist):
    sorted_list = sorted(alist)
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2.0
    else:
        return sorted_list[length // 2]

def median(root, level):
    if not root:
        return 0

    queue = Queue.Queue(maxsize=0)
    queue2 = Queue.Queue(maxsize=0)

    queue2.put(root)
    index = 0

    while not queue2.empty():
        queue2, queue = queue, queue2
        summation = []
        while not queue.empty():
            node = queue.get()
            summation.append(node.val)
            if node.left:
                queue2.put(node.left)
            if node.right:
                queue2.put(node.right)

        if index == level:
            return compute_median(summation)
        index += 1

    return 0