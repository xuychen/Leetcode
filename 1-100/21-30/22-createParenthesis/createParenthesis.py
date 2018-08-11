class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        return self.generateInOrder(n, n, "")
    
    def generateInOrder(self, numOfLeft, numOfRight, string):
        if numOfLeft == 0:
            return [string + ")" * numOfRight]
        if numOfRight < numOfLeft:
            return []
        
        return self.generateInOrder(numOfLeft-1, numOfRight, string + "(")\
                + self.generateInOrder(numOfLeft, numOfRight-1, string + ")")