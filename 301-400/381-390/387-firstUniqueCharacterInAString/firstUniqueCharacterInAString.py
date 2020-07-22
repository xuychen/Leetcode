class DoublyLinkedListNode(object):
    def __init__(self, index):
        self.index = index
        self.prev = None
        self.next = None

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        head, end = None, None
        dictionary = {}

        for i, char in enumerate(s):
            if char not in dictionary:
                if not head:
                    head = end = DoublyLinkedListNode(i)
                else:
                    end.next = DoublyLinkedListNode(i)
                    end.next.prev = end
                    end = end.next

                dictionary[char] = end
            elif dictionary[char]:
                node = dictionary[char]
                if node.prev:
                    node.prev.next = node.next
                else:
                    head = node.next

                if node.next:
                    node.next.prev = node.prev
                else:
                    end = node.prev

                dictionary[char] = None

        return head.index if head else -1

            