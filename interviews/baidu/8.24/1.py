class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_tree(root):
    return helper(root, 0)

def helper(root, value):
    if not root:
        return 0
    if not root.left and not root.right:
        return value * 10 + root.val

    node_value = value * 10 + root.val
    left = helper(root.left, node_value)
    right = helper(root.right, node_value)
    return left + right

example = TreeNode(4, TreeNode(0, TreeNode(2)), TreeNode(9))
print(sum_of_tree(example))

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    if not head:
        return head

    stack = []
    node = head
    while node:
        stack.append(node)
        node = node.next
    
    new_head = stack.pop()
    new_node = new_head

    while stack:
        new_node.next = stack.pop()
        new_node = new_node.next

    new_node.next = None
    return new_head

example = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
head = reverse(example)
node = head
while node:
    print(node.val)
    node = node.next
    