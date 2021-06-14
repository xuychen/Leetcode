class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.mins = []
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stack.append(x)
        self.mins.append(min(x, self.mins[-1]) if self.mins else x)


    def pop(self):
        """
        :rtype: None
        """

        self.mins.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """

        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()