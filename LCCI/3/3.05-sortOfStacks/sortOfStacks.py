class SortedStack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        if not self.stack:
            self.stack.append(val)
        else:
            tmp = []
            while self.stack and self.stack[-1] < val:
                tmp.append(self.stack.pop())

            self.stack.append(val)

            while tmp:
                self.stack.append(tmp.pop())


    def pop(self):
        """
        :rtype: None
        """

        if self.stack:
            self.stack.pop()


    def peek(self):
        """
        :rtype: int
        """

        return self.stack[-1] if self.stack else -1


    def isEmpty(self):
        """
        :rtype: bool
        """

        return not self.stack

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()