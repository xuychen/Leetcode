# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def merge(self, prev, head1, end1, head2, end2):
        node1, node2 = head1, head2

        if head2.val < head1.val:
            if prev:
                prev.next = head2

            head = head2
            node2 = node2.next
        else:
            head = head1
            node1 = node1.next

        prev2 = head
        while node1 != end1.next and node2 != end2.next:
            if node1.val < node2.val:
                prev2.next = node1
                node1 = node1.next
            else:
                prev2.next = node2
                node2 = node2.next

            prev2 = prev2.next

        if node1 == end1.next:
            prev2.next = node2
            end = end2
        else:
            end1.next = end2.next
            prev2.next = node1
            end = end1
        return head, end

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        increase = 1
        while True:
            node = head
            prev = None
            while node:
                head1 = head2 = node
                end1 = head1
                for i in range(increase):
                    end1 = head2
                    head2 = head2.next
                    if not head2:
                        break

                node = end2 = head2
                if not node:
                    break

                for i in range(increase):
                    end2 = node
                    node = node.next
                    if not node:
                        break

                new_head, new_end = self.merge(prev, head1, end1, head2, end2)
                if not prev:
                    head = new_head

                prev = new_end

            increase <<= 1
            if not prev and not head2:
                return head

        return head

class Solution2(object):
    def merge(self, head1, head2):
        if not head1 or not head2:
            return head1 or head2
        if head1.val > head2.val:
            return self.merge(head2, head1)

        node1, node2 = head1.next, head2
        node = head1
        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next

            node = node.next

        node.next = node1 if node1 else node2
        return head1

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        increase = 1
        while increase < length:
            node = head
            prev = None
            while node:
                head1 = end1 = node
                for i in range(increase):
                    end1 = node
                    node = node.next
                    if not node:
                        break

                end1.next = None
                end2 = head2 = node
                if node:
                    for i in range(increase):
                        end2 = node
                        node = node.next
                        if not node:
                            break

                    end2.next = None

                new_head = self.merge(head1, head2)
                if not prev:
                    prev = head = new_head
                else:
                    prev.next = new_head

                while prev.next:
                    prev = prev.next

            increase <<= 1

        return head