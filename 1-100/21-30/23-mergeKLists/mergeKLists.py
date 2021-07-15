import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        array = []
        dummy_head = ListNode(None)
        node = dummy_head

        for i, start in enumerate(lists):
            if start:
                heapq.heappush(array, (start.val, i))
                lists[i] = start.next

        while array:
            value, index = heapq.heappop(array)
            node.next = ListNode(value)
            node = node.next

            if lists[index]:
                heapq.heappush(array, (lists[index].val, index))
                lists[index] = lists[index].next

        return dummy_head.next
