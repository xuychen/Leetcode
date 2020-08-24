import itertools
import re
from operator import add, sub, mul

class Solution(object):
    def __init__(self):
        self.operators = {"+": add, "-": sub, "*": mul}
        self.result = {}
    
    def compute(self, x, y, operator):
        return self.operators[operator](x, y)
    
    def calculate(self, array, start, end):
        if (start, end) in self.result:
            return self.result[(start, end)]
        if start + 1 == end:
            return [array[start]]
        
        result = []
        for i in range(start+1, end, 2):
            left = self.calculate(array, start, i)
            right = self.calculate(array, i+1, end)
            for left, right in itertools.product(left, right):
                result.append(self.compute(left, right, array[i]))
            
        self.result[(start, end)] = result
        return result     
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        array = re.split('(\D)', input)
        length = len(array)
        array[:length:2] = map(int, array[:length:2])
        return self.calculate(array, 0, length)