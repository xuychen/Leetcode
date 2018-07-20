class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.mins = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.vals.append(x)
        if len(self.mins) == 0:
            self.mins.append(x)
        else:
            prev = self.mins[-1]
            if prev > x:
                minVal = x
            else:
                minVal = prev
            self.mins.append(minVal)
        

    def pop(self):
        """
        :rtype: void
        """
        
        if len(self.vals) == 0:
            print "Error"
        else:
            self.vals.pop()
            self.mins.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.vals[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()