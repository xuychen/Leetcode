class DoublyLinkedListNode(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def remove(self, node):
        if self.size == 1:
            self.head = self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.size -= 1

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.doublyll = DoublyLinkedList()
        self.table = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            get_node = self.table[key]
            self.doublyll.remove(get_node)
            self.doublyll.insert_head(get_node)
            return get_node.value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key not in self.table:
            if self.doublyll.size == self.capacity:
                delete_node = self.doublyll.tail
                self.doublyll.remove(delete_node)
                del self.table[delete_node.key]

            new_node = DoublyLinkedListNode(key, value)
            self.doublyll.insert_head(new_node)
            self.table[key] = new_node
        else:
            update_node = self.table[key]
            update_node.value = value
            self.doublyll.remove(update_node)
            self.doublyll.insert_head(update_node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)