class MinHeap(object):
    def __init__(self, a_list):
        self.length = len(a_list)
        self.data = a_list

        if self.data:
            for i in range(self.length/2, -1, -1):
                self.adjust_down(i)

    def adjust_down(self, parent):
        while parent < self.length / 2:
            left = parent * 2 + 1
            right = parent * 2 + 2
            left_num = self.data[left]
            right_num = self.data[right] if right < self.length else float('inf')
            if self.data[parent] <= min(left_num, right_num):
                return
            if left_num < right_num:
                self.data[parent], self.data[left] = left_num, self.data[parent]
                parent = left
            else:
                self.data[parent], self.data[right] = right_num, self.data[parent]
                parent = right

    def insert(self, num):
        self.data.append(num)
        self.length += 1

        child, parent = self.length-1, (self.length - 2) / 2
        while child and self.data[child] < self.data[parent]:
            self.data[child], self.data[parent] = self.data[parent], self.data[child]
            child = parent
            parent = (child - 1) / 2

    def top(self):
        return self.data[0] if self.length else None

    def pop_min(self):
        if not self.length:
            return None

        self.length -= 1
        result = self.data.pop()
        if not self.length:
            return result

        result, self.data[0] = self.data[0], result
        self.adjust_down(0)
        return result

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        min_heap = MinHeap(arr)
        return [min_heap.pop_min() for _ in range(k)]