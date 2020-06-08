import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.qe = Queue.Queue(maxsize=0)


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """

        self.qe.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """

        for _ in range(self.qe.qsize()-1):
            elem = self.qe.get()
            self.qe.put(elem)

        return self.qe.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """

        for _ in range(self.qe.qsize()):
            elem = self.qe.get()
            self.qe.put(elem)

        return elem

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

        return self.qe.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()