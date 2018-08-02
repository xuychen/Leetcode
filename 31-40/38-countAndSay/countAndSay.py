class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        num = "1"
        
        for _ in range(1, n):
            digit = num[0]
            count = 1
            newNum = ""
            for j in range(1, len(num)):
                if num[j] == digit:
                    count += 1
                else:
                    newNum += str(count) + digit
                    digit = num[j]
                    count = 1
                
            newNum += str(count) + digit
            num = newNum
            
        return num